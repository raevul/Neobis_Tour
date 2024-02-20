from django.urls import path, include
from djoser.views import UserViewSet

from .views import UserProfileAPIView


urlpatterns = [
    path('auth/register/', UserViewSet.as_view({'post': 'create'})),
    path('auth/me/', UserProfileAPIView.as_view()),
    path('auth/', include('djoser.urls.authtoken')),
]
