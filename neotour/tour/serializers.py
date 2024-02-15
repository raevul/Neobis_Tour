from rest_framework import serializers

from .models import Category, Tour


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['title']


class TourSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tour
        fields = ['title', 'image']


class TourDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tour
        fields = '__all__'
