from django.urls import path
from the_myeongdong import views

urlpatterns = [
    path("main", views.Main, name="main"),
]
