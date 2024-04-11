from django.urls import path
from the_myeongdong import views

urlpatterns = [
    path("reservations", views.reservation, name="reservations"),
    path("reservations/register", views.register, name="register"),
]
