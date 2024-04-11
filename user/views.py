from django.shortcuts import render
from django.http import HttpResponseRedirect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth import login, logout
from django.urls import reverse
from django.shortcuts import redirect
from .models import User


class UserLogin(APIView):
    template_name = "pages/login.html"
    success_url = "/main"

    def get(self, request):
        # GET 요청을 처리하기 위해 템플릿을 렌더링
        return render(request, self.template_name)

    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")
        try:
            user = User.objects.get(email=email.strip().lower())
        except User.DoesNotExist:
            return Response(
                {"error": "존재하지 않는 유저거나 비밀번호가 맞지 않습니다."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        if user.check_password(password):
            # 로그인 처리
            login(request, user)
            return HttpResponseRedirect(self.success_url)
        else:
            return Response(
                {"error": "존재하지 않는 유저거나 비밀번호가 맞지 않습니다."},
                status=status.HTTP_400_BAD_REQUEST,
            )


class UserLogout(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        logout(request)
        return redirect(reverse("login"))
