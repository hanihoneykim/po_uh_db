from django.shortcuts import render
from datetime import date, datetime
from rest_framework import generics, status
from django.core.paginator import Paginator
from .models import MyeongdongReservation


def Main(request):
    context = {}
    return render(request, "pages/index.html", context)


def reservation(request):
    context = {}
    return render(request, "pages/myeongdong_reservation.html", context)


def register(request):
    context = {}
    return render(request, "pages/myeongdong_register.html", context)


class ReservationListView(generics.ListCreateAPIView):
    template_name = "pages/myeongdong_reservation.html"

    def get(self, request):
        reservations = MyeongdongReservation.objects.all()
        return render(
            request, "pages/myeongdong_reservation.html", {"reservations": reservations}
        )
