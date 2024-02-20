from django.urls import path

from .views import TourAPIView, TourDetailAPIView, CategoryAPIView

urlpatterns = [
    path('tours/', TourAPIView.as_view()),
    path('tours/<int:tour_id>/', TourDetailAPIView.as_view()),
    path('category/', CategoryAPIView.as_view()),
]
