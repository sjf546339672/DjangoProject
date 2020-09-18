import json

from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.versioning import BaseVersioning, QueryParameterVersioning, URLPathVersioning
from rest_framework.parsers import JSONParser, FormParser
from rest002.models import *
from rest_framework import serializers
from rest_framework.pagination import PageNumberPagination


# class ParamVersion(object):
#
#     def determine_version(self, request, *args, **kwargs):
#         version = request.query_params.get("version")
#         return version


class RolesSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()


# class UserInfoSerializer(serializers.Serializer):
#     # user_type = serializers.IntegerField()  # 要求显示汉字
#     # type = serializers.CharField(source="user_type")
#     type = serializers.CharField(source="get_user_type_display")
#     username = serializers.CharField()
#     password = serializers.CharField()
#     group = serializers.CharField(source="group.title")
#     # roles = serializers.CharField(source="roles.all")
#     roles = serializers.SerializerMethodField()  # 自定义显示
#
#     def get_roles(self, row):
#         role_list = row.roles.all()
#         list1 = []
#         for i in role_list:
#             list1.append({"id": i.id, "title": i.title})
#         return list1

class UserInfoSerializer(serializers.ModelSerializer):
    # type = serializers.CharField(source="get_user_type_display")
    # group = serializers.CharField(source="group.title")
    # roles = serializers.SerializerMethodField()
    group = serializers.HyperlinkedIdentityField(view_name="groupqwe", lookup_field='group_id', lookup_url_kwarg="pk")

    class Meta:
        model = UserInfo
        fields = ["id", "username", "password", "user_type", "group", "roles"]
        # depth = 1


    # def get_roles(self, row):
    #     role_list = row.roles.all()
    #     list1 = []
    #     for role in role_list:
    #         list1.append({"id": role.id, "title": role.title})
    #     return list1


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserGroup
        fields = "__all__"


class UserView(APIView):
    # versioning_class = ParamVersion
    # versioning_class = QueryParameterVersioning  # 内置的
    # versioning_class = URLPathVersioning

    def get(self, request, *args, **kwargs):
        print(request.version)
        return HttpResponse("11111")


class ParseView(APIView):
    parser_classes = [JSONParser, FormParser]

    def post(self, request, *args, **kwargs):
        print(request.data)
        return HttpResponse("2222")


class RoleView(APIView):

    def get(self, request, *args, **kwargs):
        # 方法一
        # roles = Role.objects.all().values("id", "title")
        # roles = list(roles)
        # ret = json.dumps(roles, ensure_ascii=False)

        # 方法二
        # roles = Role.objects.all()
        # serializer = RolesSerializer(instance=roles, many=True)
        role = Role.objects.all().first()
        print(role.title)
        serializer = RolesSerializer(instance=role, many=False)
        return HttpResponse(serializer.data)


class UserInfoView(APIView):

    def get(self, request, *args, **kwargs):
        print(111111111)
        userinfo = UserInfo.objects.all()
        serializer = UserInfoSerializer(userinfo, many=True, context={'request': request})
        ret = json.dumps(serializer.data, ensure_ascii=False)
        return HttpResponse(ret)


class GroupView(APIView):

    def get(self, request, *args, **kwargs):
        pk = int(kwargs.get("pk"))
        print("------------------", pk)
        obj = UserGroup.objects.filter(pk=pk).first()
        ser = GroupSerializer(instance=obj, many=False)
        ret = json.dumps(ser.data, ensure_ascii=False)
        return HttpResponse(ret)


class PageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = "__all__"


class PagesView(APIView):

    def get(self, request, *args, **kwargs):
        role_list = Role.objects.all()

        pagination = PageNumberPagination()
        page_role_list = pagination.paginate_queryset(queryset=role_list, request=request, view=self)
        serializer = PageSerializer(instance=page_role_list, many=True)
        return pagination.get_paginated_response(serializer.data)


from rest_framework.generics import GenericAPIView


class View1View(GenericAPIView):
    queryset = Role.objects.all()
    serializer_class = PageSerializer
    pagination_class = PageNumberPagination

    def get(self, request, *args, **kwargs):
        role_list = self.get_queryset()
        page_roles = self.paginate_queryset(role_list)
        ser = self.get_serializer(instance=page_roles, many=True)
        return Response(ser.data)


from rest_framework.viewsets import GenericViewSet, ModelViewSet


class View2View(ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = PageSerializer
    pagination_class = PageNumberPagination
