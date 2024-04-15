from django.shortcuts import render
from django.db.models import Q
from datetime import date, datetime
from rest_framework import generics, status
from django.core.paginator import Paginator
from .models import MyeongdongReservation
from .serializers import MyeongdongReservationSerialzier


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


class ReservationDetailView(generics.RetrieveUpdateDestroyAPIView):
    template_name = "pages/myeongdong_detail.html"
    serializer_class = MyeongdongReservationSerialzier
    queryset = MyeongdongReservation.objects.all()
    lookup_field = "pk"

    def get(self, request, pk):
        reservation = MyeongdongReservation.objects.get(pk=pk)

        again_guest = MyeongdongReservation.objects.filter(
            guest_name=reservation.guest_name,
            phone_number=reservation.phone_number,
            email=reservation.email,
        ).exclude(
            pk=pk
        )  # 현재 조회중인 예약은 제외합니다.

        return render(
            request,
            "pages/myeongdong_detail.html",
            {"reservation": reservation, "again_guest": again_guest},
        )
