# coding: utf-8
from django.urls import path
from . import views

urlpatterns = [
    path("auth/", views.AuthView.as_view(), name="auth"),
    path("order/", views.OrderView.as_view(), name="order"),
    path("info/", views.InfoView.as_view(), name="info"),
]
