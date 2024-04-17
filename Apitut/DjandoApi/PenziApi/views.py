from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from PenziApi.models import Users, Messages
from PenziApi.serializers import UsersSerializer, MessagesSerializer
from django.core.files.storage import default_storage

# Create your views here.


@csrf_exempt
def UsersApi(request, id=0):
    if request.method == "GET":
        users_data = Users.objects.all()
        users_serializer = UsersSerializer(users_data, many=True)
        return JsonResponse(users_serializer.data, safe=False)
    elif request.method == "POST":
        users_data = JSONParser().parse(request)
        users_serializer = UsersSerializer(data=users_data)
        if users_serializer.is_valid():
            users_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method == "PUT":
        users_data = JSONParser().parse(request)
        users_data = Users.objects.get(user_id=users_data["user_id"])
        users_serializer = UsersSerializer(users_data, data=users_data)
        if users_serializer.is_valid():
            users_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update")
    elif request.method == "DELETE":
        users_data = Users.objects.get(user_id=id)
        users_data.delete()
        return JsonResponse("Deleted Successfully", safe=False)


@csrf_exempt
def MessagesApi(request, id=0):
    if request.method == "GET":
        messages_data = Messages.objects.all()
        messages_serializer = MessagesSerializer(messages_data, many=True)
        return JsonResponse(messages_serializer.data, safe=False)
    elif request.method == "POST":
        messages_data = JSONParser().parse(request)
        messages_serializer = MessagesSerializer(data=messages_data)
        messages_serializer.is_valid(raise_exception=True)

        if messages_serializer.is_valid():

            message_txt = messages_data.get(
                "message_txt", ""
            ).lower()  # Define the variable "message_txt"

            response_data = {}  # Define the variable "response_data"
            if "penzi" == message_txt:
                response_data = {
                    "response": "Welcome to our dating service with 6000 potential dating partners! To register, SMS start #name#age#gender#county#town to 22141. Eg start #John Doe#25#male#Nairobi#Kasarani"
                }
                return JsonResponse(response_data, safe=False)
            elif "start" in message_txt:

                # extract the user data from the message and create a new user instance
                user_details = message_txt.split("#")[1:]
                user_data = {
                    "username": user_details[0],
                    "age": user_details[1],
                    "gender": user_details[2],
                    "county": user_details[3],
                    "town": user_details[4],
                }
                users_serializer = UsersSerializer(data=user_data)
                if users_serializer.is_valid():
                    users_serializer.save()
                    response_data = {
                        "response": "Your profile has been created successfully. SMS details#levelOfEducation#profession#maritalStatus#religion#ethnicity to 22141. Eg details#degree#engineer#single#christian#kamba"
                    }
                    return JsonResponse(response_data, safe=False)
                else:
                    return JsonResponse("Failed to Create User", status=400)
            elif "details" in message_txt:
                user_details = message_txt.split("#")[1:]
                user_id = messages_data.get("user_id", None)
                if user_id is not None:
                    try:
                        # retrieve the user data from the database
                        user_data = Users.objects.get(user_id=user_id)
                        # update the user data with the new details
                        user_data.level_of_edu = user_details[0]
                        user_data.profesion = user_details[1]
                        user_data.marital_stat = user_details[2]
                        user_data.religion = user_details[3]
                        user_data.ethnicity = user_details[4]
                        user_data.save()
                        print(user_data)
                        response_data = {
                            "response": "Your profile has been updated successfully. SMS match to 22141 to get your dating partner"
                        }
                        return JsonResponse(response_data, safe=False)
                    except Users.DoesNotExist:
                        return JsonResponse("User not found", status=404)
                else:
                    if user_id is None:
                        response_data = {
                            "response": "You have not registered. SMS start #name#age#gender#county#town to 22141. Eg start #John Doe#25#male#Nairobi#Kasarani"
                        }
                        return JsonResponse(response_data, safe=False)
    elif request.method == "PUT":
        messages_data = JSONParser().parse(request)
        messages_data = Messages.objects.get(message_id=messages_data["message_id"])
        messages_serializer = MessagesSerializer(messages_data, data=messages_data)
        if messages_serializer.is_valid():
            messages_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update")
    elif request.method == "DELETE":
        messages_data = Messages.objects.get(message_id=id)
        messages_data.delete()
        return JsonResponse("Deleted Successfully", safe=False)
    return JsonResponse("Invalid request", safe=False, status=400)
