from djoser.serializers import UserCreateSerializer
from rest_framework import serializers

from reserve.serializers import ReserveSerializer
from .models import UserProfile


class CustomUserRegistrationSerializer(UserCreateSerializer):
    phone = serializers.CharField(max_length=13, read_only=True)
    reserve = ReserveSerializer(many=True, read_only=True)

    class Meta:
        model = UserProfile
        fields = ['id', 'username', 'email', 'password', 'phone', 'reserve']
