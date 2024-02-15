from django.urls import path

from .views import TourAPIView, TourDetailAPIView

urlpatterns = [
    path('tours/', TourAPIView.as_view()),
    path('tours/<int:tour_id>/', TourDetailAPIView.as_view()),
]
