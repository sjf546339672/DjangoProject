# coding: utf-8
from django.urls import path
from .views import student_register_view

urlpatterns = [
    path("studentregister/", student_register_view, name="studentregister"),
]




