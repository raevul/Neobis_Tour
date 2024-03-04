from django.urls import path, include

from .views import UserProfileAPIView, RegisterAPIView


urlpatterns = [
    path('auth/register/', RegisterAPIView.as_view()),
    path('auth/me/', UserProfileAPIView.as_view()),
    path('auth/', include('djoser.urls.authtoken')),
]
