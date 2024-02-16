from rest_framework import views, status
from rest_framework.response import Response

from .serializers import CategorySerializer, TourSerializer, TourDetailSerializer
from .models import Category, Tour


class TourAPIView(views.APIView):

    def get(self, request):
        categories = Category.objects.all()
        tours = Tour.objects.all()
        try:
            category_serializer = CategorySerializer(categories, many=True)
            tour_serializer = TourSerializer(tours, many=True)
        except Exception as a:
            return Response({'data': 'Bad request'}, status=status.HTTP_400_BAD_REQUEST)

        content = {'categories': category_serializer.data,
                   'tours': tour_serializer.data}
        return Response(content, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = TourDetailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TourDetailAPIView(views.APIView):
    def get(self, request, *args, **kwargs):
        try:
            tour = Tour.objects.get(id=kwargs['tour_id'])
        except Exception as e:
            return Response({"data": "Page not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = TourDetailSerializer(tour)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        tour = Tour.objects.get(id=kwargs['tour_id'])
        serializer = TourDetailSerializer(instance=tour, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        try:
            tour = Tour.objects.get(id=kwargs['tour_id'])
        except Exception as e:
            return Response({'data': 'Error when deleting'}, status=status.HTTP_400_BAD_REQUEST)
        tour.delete()
        return Response({'data': 'Successfully deleted'}, status=status.HTTP_200_OK)
