from django.urls import path, include
from djoser.views import UserViewSet

from .views import CustomUserViewSet


urlpatterns = [
    path('auth/register/', UserViewSet.as_view({'post': 'create'})),
    path('auth/me/', CustomUserViewSet.as_view({'get': 'me'})),
    path('auth/', include('djoser.urls.authtoken')),
]
