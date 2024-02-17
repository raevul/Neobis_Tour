from rest_framework import serializers
from phonenumber_field.serializerfields import PhoneNumberField

from .models import Reserve


class ReserveSerializer(serializers.ModelSerializer):
    phone = PhoneNumberField(region="KG")

    class Meta:
        model = Reserve
        fields = '__all__'
