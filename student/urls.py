
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("index/", views.index, name="index"),
    path("register/", views.register, name="register"),
    path("show/", views.show_view, name="show"),
    path("login/", views.login_view, name="login"),
]
