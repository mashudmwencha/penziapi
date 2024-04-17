from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.


@api_view(["POST"])
def HandleSms(request):
    if request.method == "POST":
        data = request.data.get("data")
        if data.lower() == "penzi":
            return Response(
                {
                    "Welcome to our dating service with 6000 potential dating partners!To register, SMS start #name#age#gender#county#town to 22141.Eg start #John Doe#25#male#Nairobi#Kasarani"
                }
            )
        else:
            pass
