# coding: utf-8
from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path(r"^(?P<version>[v1|v2|v3]+)/users/$", views.UserView.as_view(), name="users"),
    re_path(r"^(?P<version>[v1|v2|v3]+)/parse/$", views.ParseView.as_view(), name="parse"),
    re_path(r"^(?P<version>[v1|v2|v3]+)/roles/$", views.RoleView.as_view(), name="role"),
    path("userinfo/", views.UserInfoView.as_view(), name="userinfo"),
    path("group/<str:pk>/", views.GroupView.as_view(), name="groupqwe"),
    path("pages/", views.PagesView.as_view()),
    path("view1/", views.View1View.as_view()),
    path("view2/", views.View2View.as_view({'get': 'list', "post": "create"})),
    path("view2/<int:pk>/", views.View2View.as_view(
        {'get': 'retrieve', "delete": "destroy", "put": "update",
         "patch": "partial_update"})),
]

