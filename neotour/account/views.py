from django.contrib.auth.models import User
from rest_framework import views, status
from rest_framework.response import Response
from djoser.permissions import CurrentUserOrAdminOrReadOnly

from .serializers import UserProfileSerializer
from .models import UserProfile


class RegisterAPIView(views.APIView):
    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')

        user = User.objects.create(username=username, email=email)
        user.set_password(password)
        user.save()

        profile_data = {'user': user.id}
        profile_serializer = UserProfileSerializer(data=profile_data)
        if profile_serializer.is_valid():
            profile_serializer.save()
            return Response(profile_serializer.data, status=status.HTTP_201_CREATED)
        else:
            user.delete()
            return Response(profile_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserProfileAPIView(views.APIView):
    permission_classes = [CurrentUserOrAdminOrReadOnly]

    def get(self, request, *args, **kwargs):
        try:
            user = UserProfile.objects.get(user=request.user)
        except UserProfile.DoesNotExist:
            return Response({"data": "Profile does not exist"}, status=status.HTTP_404_NOT_FOUND)
        serializer = UserProfileSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
