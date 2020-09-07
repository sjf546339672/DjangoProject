# coding: utf-8
from django.urls import path
from . import views


urlpatterns = [
    path("index/", views.index_view, name="index"),
    path("query1/<int:year>/<int:month>/", views.query1_view, name="query1"),
    path("query2/<int:year>/<int:month>/", views.query2_view, {"name": "zhangsan"}, name="query2"),
]
