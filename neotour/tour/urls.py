from django.urls import path

from .views import TourAPIView, TourDetailAPIView, CategoryAPIView, CategoryDetailAPIView, TourReservationAPIView

urlpatterns = [
    path('tours/', TourAPIView.as_view()),
    path('tours/<int:tour_id>/', TourDetailAPIView.as_view()),
    path('tours/reservation/<int:tour_id>/', TourReservationAPIView.as_view()),
    path('category/', CategoryAPIView.as_view()),
    path('category/<str:title>/', CategoryDetailAPIView.as_view()),
]
