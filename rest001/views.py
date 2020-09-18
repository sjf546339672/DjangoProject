import json
import time

from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from rest_framework import exceptions
from rest_framework.views import APIView
from rest001.models import UserInfo, UserToken

ORDER_DICT = {
    1: {
        "name": "狗",
        "age": "1",
        "gender": "男",
        "content": "...",
    },
    2: {
            "name": "猫",
            "age": "2",
            "gender": "女",
            "content": "...",
        }
}


def md5(user):
    import hashlib
    ctime = time.time()
    m = hashlib.md5(bytes(user, encoding="utf-8"))
    m.update(bytes(str(ctime), encoding="utf-8"))
    return m.hexdigest()


class AuthView(APIView):
    """用于用户登录认证"""
    def post(self, request, *args, **kwargs):
        ret = {"code": 1000, "msg": None}
        try:
            user = request.POST.get("username")
            pwd = request.POST.get("password")
            obj = UserInfo.objects.filter(username=user, password=pwd).first()
            if not obj:
                ret["code"] = 1001
                ret["msg"] = "用户名密码错误"
            token = md5(user)
            UserToken.objects.update_or_create(user=obj, defaults={"token": token})
            ret["token"] = token
        except Exception as e:
            ret["code"] = 1002
            ret["msg"] = "请求异常"
        return JsonResponse(ret)


class Authtication(object):

    def authenticate(self, request):
        token = request._request.POST.get("token")
        token_obj = UserToken.objects.filter(token=token).first()
        if not token_obj:
            raise exceptions.AuthenticationFailed("用户认证失败")
        return (token_obj.user, token_obj)

    def authenticate_header(self, request):
        pass


class OrderView(APIView):
    """用于订单相关业务"""
    # authentication_classes = [Authtication, ]

    def get(self, request, *args, **kwargs):
        print(11111, request.user)

        if request.user.user_type != 3:
            return HttpResponse("无权访问")

        ret = {"code": 1000, "msg": None}
        try:
            ret["data"] = ORDER_DICT
        except Exception as e:
            pass
        return JsonResponse(ret)


class InfoView(APIView):
    """订单相关业务"""
    def get(self, request, *args, **kwargs):
        print(request.user)
        return HttpResponse("用户信息")



