from djoser.views import UserViewSet as DjoserUserViewSet

from .serializers import CustomUserRegistrationSerializer


class CustomUserViewSet(DjoserUserViewSet):
    serializer_class = CustomUserRegistrationSerializer

    def get_serializer_class(self):
        if self.action == 'me':
            return CustomUserRegistrationSerializer
        return super().get_serializer_class()

    def get_queryset(self):
        return self.request.user
