from django.urls import path

from .views import ReserveAPIView


urlpatterns = [
    path('reserve/', ReserveAPIView.as_view())
]
