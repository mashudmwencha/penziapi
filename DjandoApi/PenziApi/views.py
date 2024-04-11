from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from PenziApi.models import Users, Messages
from PenziApi.serializers import UsersSerializer, MessagesSerializer

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
        if messages_serializer.is_valid():
            messages_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
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
