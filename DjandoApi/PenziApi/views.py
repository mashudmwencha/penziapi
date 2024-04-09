from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from PenziApi.models import Users, messages
from PenziApi.serializers import UsersSerailizer, MessagesSerializer

# Create your views here.


@csrf_exempt
def PenziApi(request, id=0):
    if request.method == "GET":
        users_data = Users.objects.all()
        users_serializer = UsersSerailizer(users_data, many=True)
        return JsonResponse(users_serializer.data, safe=False)
    elif request.method == "POST":
        users_data = JSONParser().parse(request)
        users_serializer = UsersSerailizer(data=users_data)
        if users_serializer.is_valid():
            users_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method == "PUT":
        users_data = JSONParser().parse(request)
        users_data = Users.objects.get(user_id=users_data["user_id"])
        users_serializer = UsersSerailizer(users_data, data=users_data)
        if users_serializer.is_valid():
            users_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update")
    elif request.method == "DELETE":
        users_data = Users.objects.get(user_id=id)
        users_data.delete()
        return JsonResponse("Deleted Successfully", safe=False)
