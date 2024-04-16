from django.urls import path
from the_myeongdong import views

urlpatterns = [
    # path("reservations", views.reservation, name="reservations"),
    path(
        "reservations",
        views.MyeongdongReservationListView.as_view(),
        name="reservations",
    ),
    path("reservations/register", views.register, name="register"),
    path("reservations/status", views.reservation_status, name="status"),
    path(
        "reservations/<str:pk>",
        views.MyeongdongReservationDetailView.as_view(),
        name="reservation_detail",
    ),
]
