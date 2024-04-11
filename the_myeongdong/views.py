from django.shortcuts import render
from datetime import date, datetime
from rest_framework import generics, status
from django.core.paginator import Paginator


def Main(request):
    context = {}
    return render(request, "pages/index.html", context)


def reservation(request):
    context = {}
    return render(request, "pages/myeongdong_reservation.html", context)


def register(request):
    context = {}
    return render(request, "pages/myeongdong_register.html", context)
