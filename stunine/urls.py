# coding: utf-8
from django.urls import path

from . import views


urlpatterns = [
    path("index/", views.IndexViews.as_view(), name="index"),
    path("index2/", views.IndexViews2.as_view(), name="index2"),
    path("index3/", views.IndexViews3.as_view(), name="index3"),
    path("index4/", views.IndexViews4.as_view(), name="index4"),
    path("index5/", views.IndexViews5.as_view(), name="index5"),
]





