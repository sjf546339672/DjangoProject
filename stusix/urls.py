# coding: utf-8
from django.conf.urls import url
from django.urls import path, re_path
from . import views
from DjangoProject.settings import DEBUG, MEDIA_ROOT

urlpatterns = [
    path("uploadimg/", views.upload_img_view, name="uploadimg"),
    path("showall/", views.show_all_view, name="showall"),
    path("downloadimg/", views.download_img_view, name="downloadimg"),
]



