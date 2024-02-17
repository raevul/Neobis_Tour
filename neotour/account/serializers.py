from djoser.serializers import UserCreateSerializer
from django.contrib.auth import get_user_model
from rest_framework import serializers

from reserve.models import Reserve


class CustomUserRegistrationSerializer(UserCreateSerializer):
    phone = serializers.CharField(max_length=13)
    reserve = serializers.PrimaryKeyRelatedField(queryset=Reserve.objects.all(), many=True)

    class Meta(UserCreateSerializer.Meta):
        model = get_user_model()
        fields = ['id', 'username', 'email', 'password', 'phone', 'reserve']
