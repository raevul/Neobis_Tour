from rest_framework import serializers

from reserve.serializers import ReserveSerializer
from .models import UserProfile


class UserProfileSerializer(serializers.ModelSerializer):
    reserve = ReserveSerializer(read_only=True)

    class Meta:
        model = UserProfile
        fields = ['id', 'username', 'email', 'reserve']
