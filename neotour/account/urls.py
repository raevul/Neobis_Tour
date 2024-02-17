from django.urls import path, include
from djoser.views import UserViewSet


urlpatterns = [
    path('auth/register/', UserViewSet.as_view({'post': 'create'})),
    path('auth/me/', UserViewSet.as_view({'get': 'me'})),
    path('auth/', include('djoser.urls.authtoken')),
]
