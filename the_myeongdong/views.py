from django.shortcuts import render
from rest_framework.response import Response
from django.db.models import Q
from datetime import date, datetime
from rest_framework import generics, status
from django.core.paginator import Paginator
from .models import MyeongdongReservation
from .serializers import MyeongdongReservationSerializer


def Main(request):
    context = {}
    return render(request, "pages/index.html", context)


def reservation(request):
    context = {}
    return render(request, "pages/myeongdong_reservation.html", context)


def register(request):
    context = {}
    return render(request, "pages/myeongdong_register.html", context)


from django.db.models import Q
from rest_framework import generics
from django.shortcuts import render
from .models import MyeongdongReservation


class MyeongdongReservationListView(generics.ListCreateAPIView):
    template_name = "pages/myeongdong_reservation.html"
    serializer_class = MyeongdongReservationSerializer

    def get_queryset(self):
        queryset = MyeongdongReservation.objects.all()

        # 쿼리 파라미터 받아오기
        building_location_param = self.request.GET.get("building_location")
        room_type_param = self.request.GET.get("room_type")
        guest_name_param = self.request.GET.get("guest_name")
        platform_name_param = self.request.GET.get("platform_name")
        # 나머지 쿼리 파라미터들도 유사하게 처리합니다.

        # 필터링
        if building_location_param:
            queryset = queryset.filter(building_location=building_location_param)
        if room_type_param:
            queryset = queryset.filter(room_type=room_type_param)
        if guest_name_param:
            queryset = queryset.filter(guest_name__icontains=guest_name_param)
        if platform_name_param:
            queryset = queryset.filter(platform_name=platform_name_param)
        # 나머지 필터도 유사하게 처리합니다.

        return queryset

    def get(self, request):
        queryset = self.get_queryset()
        serializer = MyeongdongReservationSerializer(queryset, many=True)
        return render(
            request,
            "pages/myeongdong_reservation.html",
            {"reservations": serializer.data},
        )


class MyeongdongReservationDetailView(generics.RetrieveUpdateDestroyAPIView):
    template_name = "pages/myeongdong_detail.html"
    serializer_class = MyeongdongReservationSerializer
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
