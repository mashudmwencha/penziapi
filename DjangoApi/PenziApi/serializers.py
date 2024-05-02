from rest_framework import serializers
from .models import (
    User,
    ReceivedMessage,
    UserProfile,
    UserDetails,
    UserDescription,
    Message,
)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class ReceivedMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReceivedMessage
        fields = ("id", "user", "message", "timestamp")


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = "__all__"


class UserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDetails
        fields = (
            "id",
            "user",
            "level_of_education",
            "profession",
            "marital_status",
            "religion",
            "ethnicity",
        )


class UserDescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDescription
        fields = ("id", "user", "description_text")


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ["id", "sender", "receiver", "message", "timestamp"]


class MergedUserDataSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=100)
    age = serializers.IntegerField()
    gender = serializers.CharField(max_length=10)
    county = serializers.CharField(max_length=100)
    town = serializers.CharField(max_length=100)
    level_of_education = serializers.CharField(max_length=100)
    profession = serializers.CharField(max_length=100)
    marital_status = serializers.CharField(max_length=100)
    religion = serializers.CharField(max_length=100)
    ethnicity = serializers.CharField(max_length=100)
    created_at = serializers.DateTimeField()
