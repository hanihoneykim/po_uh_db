from django.urls import path
from core import views
from user.views import UserLogin
from the_myeongdong.views import Main

urlpatterns = [
    path("", UserLogin.as_view(), name="login"),
    path("main", Main, name="main"),
    path("guest_inquiry", Main, name="guest_inquiry"),
]
