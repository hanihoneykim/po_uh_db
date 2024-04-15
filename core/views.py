from django.shortcuts import render
from rest_framework.response import Response
from django.http import HttpResponseRedirect
from django.db.models import Q
from datetime import date, datetime
from rest_framework import generics, status
from django.core.paginator import Paginator
from .models import Guest
from .serializers import GuestSerializer


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

        # 쿼리셋에 필터를 적용합니다.
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
            # 아무 데이터도 가져오지 않습니다.
            queryset = Guest.objects.none()
            serializer = GuestSerializer(queryset, many=True)
            return render(request, self.template_name, {"guests": serializer.data})

        # 파라미터가 있는 경우
        queryset = self.get_queryset()
        serializer = GuestSerializer(queryset, many=True)
        return render(request, self.template_name, {"guests": serializer.data})
