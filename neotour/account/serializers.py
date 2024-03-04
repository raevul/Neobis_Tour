from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from reserve.serializers import ReserveSerializer
from .models import UserProfile


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(write_only=True)
    password = serializers.CharField(write_only=True, min_length=8, max_length=15)
    confirm_password = serializers.CharField(write_only=True, min_length=8, max_length=16)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'confirm_password']

    def create(self, validated_data):
        password = validated_data.pop('password')
        confirm_password = validated_data.pop('confirm_password')
        if password != confirm_password:
            raise ValidationError({"data": "Пароли не совпадают"})
        if User.objects.filter(email=self.validated_data['email']).exists():
            raise ValidationError({"data": "Этот аккаунт уже зарегистирирован"})

        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        UserProfile.objects.create(user=user, username=user.username, email=user.email)
        return user


class UserProfileSerializer(serializers.ModelSerializer):
    reserve = ReserveSerializer(read_only=True)

    class Meta:
        model = UserProfile
        fields = ['id', 'username', 'email', 'reserve']
