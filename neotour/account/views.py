from rest_framework import views, status
from rest_framework.response import Response
from djoser.permissions import CurrentUserOrAdminOrReadOnly

from .serializers import UserProfileSerializer
from .models import UserProfile


class UserProfileAPIView(views.APIView):
    permission_classes = [CurrentUserOrAdminOrReadOnly]

    def get(self, request, *args, **kwargs):
        try:
            user = UserProfile.objects.get(user=request.user)
        except UserProfile.DoesNotExist:
            return Response({"data": "Profile does not exist"}, status=status.HTTP_404_NOT_FOUND)
        serializer = UserProfileSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
