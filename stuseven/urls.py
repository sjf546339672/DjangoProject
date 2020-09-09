# coding: utf-8
from django.urls import path
from . import views

urlpatterns = [
    path("setcookie/", views.setcookie_view, name="setcookie"),
    path("sevenlogin/", views.deal_login_view, name="sevenlogin"),
    path("sevensession/", views.deal_session_view, name="sevensession"),
]
