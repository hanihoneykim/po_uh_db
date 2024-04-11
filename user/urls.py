from django.urls import path
from user import views

urlpatterns = [
    path("login", views.UserLogin.as_view(), name="user_login"),
    path("logout", views.UserLogout.as_view(), name="user_logout"),
]
