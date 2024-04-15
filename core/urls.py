from django.urls import path
from core import views
from user.views import UserLogin
from the_myeongdong.views import Main

urlpatterns = [
    path("", UserLogin.as_view(), name="login"),
    path("main", Main, name="main"),
    path("branch", views.branch, name="branch"),
    path("guest_inquiry", views.GuestListView.as_view(), name="guest_inquiry"),
]
