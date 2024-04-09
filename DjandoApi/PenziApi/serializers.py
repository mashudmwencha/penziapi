from rest_framework import serializers
from PenziApi.models import Users, messages


class UsersSerailizer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = "__all__"


class MessagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = messages
        fields = "__all__"
