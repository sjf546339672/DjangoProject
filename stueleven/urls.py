# coding: utf-8
from django.urls import path
from . import views

urlpatterns = [
    path("elevenindex/", views.eleven_index, name="elevenindex")
]
