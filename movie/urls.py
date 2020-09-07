# coding: utf-8
from django.urls import path
from . import views

urlpatterns = [
    path("show/", views.show_view, name="show"),  # 原生分页展示数据
    path("showdata/", views.show_data_view, name="showdata")  # Django分页展示数据
]
