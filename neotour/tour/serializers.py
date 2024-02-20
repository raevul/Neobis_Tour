from rest_framework import serializers

from .models import Category, Tour, TourImages


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['title']


class TourImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = TourImages
        fields = '__all__'


class TourSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tour
        fields = ['title', 'image']


class TourDetailSerializer(serializers.ModelSerializer):
    images = TourImageSerializer(many=True, read_only=True)
    uploaded_images = serializers.ListField(
        child=serializers.ImageField(max_length=100000, allow_empty_file=False, use_url=False),
        write_only=True
    )

    class Meta:
        model = Tour
        fields = ['id', 'title', 'image', 'description', 'price', 'category', 'location', 'images', 'uploaded_images']

    def create(self, validated_data):
        uploaded_data = validated_data.pop('uploaded_images')
        new_tour = Tour.objects.create(**validated_data)
        for uploaded_item in uploaded_data:
            new_tour_image = TourImages.objects.create(tour=new_tour, images=uploaded_item)
        return new_tour


class CategoryDetailSerializer(serializers.ModelSerializer):
    tours = TourSerializer(many=True)

    class Meta:
        model = Category
        fields = ['id', 'title', 'tours']
