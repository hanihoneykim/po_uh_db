from django.shortcuts import render
from rest_framework.response import Response
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.db.models import Q
from datetime import date, datetime
from rest_framework import generics, status
from django.core.paginator import Paginator
from .models import Guest
from .serializers import GuestSerializer
from the_myeongdong.models import MyeongdongReservation
from the_myeongdong.serializers import MyeongdongReservationSerializer


def health_check(request):
    return HttpResponse(status=200)


def branch(request):
    context = {}
    return render(request, "pages/branch_main.html", context)


class GuestListView(generics.ListCreateAPIView):
    template_name = "pages/guest/guest_inquiry.html"
    serializer_class = GuestSerializer

    def get_queryset(self):
        queryset = Guest.objects.all()

        # 쿼리 파라미터에서 필터링에 사용할 값들을 가져옵니다.
        guest_name_param = self.request.query_params.get("guest_name", "")
        phone_number_param = self.request.query_params.get("phone_number", "")
        date_of_birth_param = self.request.query_params.get("date_of_birth", "")
        guest_type_param = self.request.query_params.get("guest_type", "")
        credit_card_number_param = self.request.query_params.get(
            "credit_card_number", ""
        )
        email_param = self.request.query_params.get("email", "")
        nationality_param = self.request.query_params.get("nationality", "")
        job_param = self.request.query_params.get("job", "")
        memo_param = self.request.query_params.get("memo", "")

        # 새로운 URL에서 기간을 가져옵니다.
        start_of_visit_date_param = self.request.query_params.get(
            "startOfVisitDate", ""
        )
        end_of_visit_date_param = self.request.query_params.get("endOfVisitDate", "")

        # 시작일과 종료일이 모두 제공되는 경우에만 예약 데이터를 가져옵니다.
        if start_of_visit_date_param and end_of_visit_date_param:
            try:
                start_date = datetime.strptime(start_of_visit_date_param, "%Y-%m-%d")
                end_date = datetime.strptime(end_of_visit_date_param, "%Y-%m-%d")

                # 시작일과 종료일 사이에 포함되는 예약 데이터를 가져옵니다.
                reservations = MyeongdongReservation.objects.filter(
                    Q(check_in_date__gte=start_date, check_in_date__lte=end_date)
                    | Q(check_out_date__gte=start_date, check_out_date__lte=end_date)
                    | Q(check_in_date__lte=start_date, check_out_date__gte=end_date)
                )

                # 예약 데이터에 연결된 고객명을 가져옵니다.
                guest_names = reservations.values_list("guest_name", flat=True)

                # 예약 데이터에 연결된 고객명과 파라미터로 받은 값이 일치하는 고객을 필터링합니다.
                if guest_names:
                    queryset = queryset.filter(guest_name__in=guest_names)

            except ValueError:
                # 날짜 형식이 잘못된 경우에 대한 처리
                pass

        # 그 외의 파라미터에 대한 필터링을 적용합니다.
        if guest_name_param:
            queryset = queryset.filter(guest_name__icontains=guest_name_param)

        if phone_number_param:
            queryset = queryset.filter(phone_number__icontains=phone_number_param)

        if date_of_birth_param:
            queryset = queryset.filter(date_of_birth__icontains=date_of_birth_param)

        if guest_type_param:
            queryset = queryset.filter(guest_type=guest_type_param)

        if credit_card_number_param:
            queryset = queryset.filter(
                credit_card_number__icontains=credit_card_number_param
            )

        if email_param:
            queryset = queryset.filter(email__icontains=email_param)

        if nationality_param:
            queryset = queryset.filter(nationality__icontains=nationality_param)

        if job_param:
            queryset = queryset.filter(job__icontains=job_param)

        if memo_param:
            queryset = queryset.filter(memo__icontains=memo_param)

        return queryset

    def get(self, request, *args, **kwargs):
        # 필터링에 사용할 파라미터들을 가져옵니다.
        guest_name_param = self.request.query_params.get("guest_name", "")
        phone_number_param = self.request.query_params.get("phone_number", "")
        date_of_birth_param = self.request.query_params.get("date_of_birth", "")
        guest_type_param = self.request.query_params.get("guest_type", "")
        credit_card_number_param = self.request.query_params.get(
            "credit_card_number", ""
        )
        email_param = self.request.query_params.get("email", "")
        nationality_param = self.request.query_params.get("nationality", "")
        job_param = self.request.query_params.get("job", "")
        memo_param = self.request.query_params.get("memo", "")

        # 모든 파라미터가 비어있는 경우
        if not any(
            [
                guest_name_param,
                phone_number_param,
                date_of_birth_param,
                guest_type_param,
                credit_card_number_param,
                email_param,
                nationality_param,
                job_param,
                memo_param,
            ]
        ):
            # 가장 최근에 생성된 10개의 데이터를 가져옵니다.
            queryset = Guest.objects.order_by("-id")[:10]
            serializer = GuestSerializer(queryset, many=True)
            return render(request, self.template_name, {"guests": serializer.data})

        # 파라미터가 있는 경우
        queryset = self.get_queryset()
        serializer = GuestSerializer(queryset, many=True)
        return render(request, self.template_name, {"guests": serializer.data})


class GuestDetailView(generics.RetrieveUpdateDestroyAPIView):
    template_name = "pages/guest/guest_detail_info.html"
    serializer_class = GuestSerializer
    queryset = Guest.objects.all()
    lookup_field = "pk"

    def get(self, request, pk):
        guest = Guest.objects.get(pk=pk)

        guest_reservations = MyeongdongReservation.objects.filter(
            Q(guest_name=guest.guest_name) | Q(phone_number=guest.phone_number)
        )

        # 포맷팅된 숫자를 guest_reservations_serializer에 추가
        guest_reservations_data = []
        for reservation in guest_reservations:
            formatted_reservation = {
                "id": reservation.id,
                "building_location": reservation.building_location,
                "room_type": reservation.room_type,
                "guest_name": reservation.guest_name,
                "platform_name": reservation.platform_name,
                "reservation_date": reservation.reservation_date,
                "lead_time": reservation.lead_time,
                "check_in_date": reservation.check_in_date,
                "check_out_date": reservation.check_out_date,
                "length_of_stay": reservation.length_of_stay,
                "total_room_charge": "{0:,.0f}".format(reservation.total_room_charge),
                "adr": "{0:,.0f}".format(reservation.adr),
                "nationality": reservation.nationality,
                "guest_count": reservation.guest_count,
                "relationship": reservation.relationship,
                "is_checked_in": reservation.is_checked_in,
                "is_minor": reservation.is_minor,
                "phone_number": reservation.phone_number,
                "email": reservation.email,
                "remarks": reservation.remarks,
            }
            guest_reservations_data.append(formatted_reservation)

        serializer = GuestSerializer(guest)
        return render(
            request,
            "pages/guest/guest_detail_info.html",
            {
                "guest": serializer.data,
                "guest_reservations": guest_reservations_data,
            },
        )
