# coding: utf-8
from django.urls import path
from . import views


urlpatterns = [
    path("tweindex", views.IndexView, name="tweindex"),
    path("topay", views.ToPayView, name="topay"),
    path("checkPay", views.checkPayView, name="checkPay"),
]
