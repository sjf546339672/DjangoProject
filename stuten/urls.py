# coding: utf-8
from django.urls import path
from . import views

urlpatterns = [
    path("tenlogin/", views.LoginView.as_view(), name="tenlogin"),
    path("tenregister/", views.RegisterView.as_view(), name="tenregister"),
]


