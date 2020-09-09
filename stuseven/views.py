import datetime

from django.http import HttpResponse
from django.shortcuts import render


def setcookie_view(request):
    # 创建一个响应对象
    response = HttpResponse()
    # response.set_cookie("uname", "zhangsan", max_age=24*60*60, path="/stuseven/hello/",expires=datetime.datetime.today()+datetime.timedelta(days=2))
    response.set_signed_cookie("uname", "zhangsan", salt="sdasdasdasda")
    return response


def deal_login_view(request):
    """处理登录"""
    if request.method == "GET":
        cookies = request.COOKIES
        if cookies:
            uname = request.COOKIES.get("uname")
            pwd = request.COOKIES.get("pwd")
            return render(request, "sevenlogin.html",
                          {"uname": uname, "pwd": pwd})

    if request.method == "POST":
        uname = request.POST.get("uname", "")
        pwd = request.POST.get("pwd", "")
        response = HttpResponse()
        if uname == "zhangsan" and pwd == "123":
            # 记住密码
            response.content = "登陆成功"
            response.set_cookie("login", uname+","+pwd, path="/stuseven/sevenlogin/", max_age=3*24*60*60)
            return response
        response.delete_cookie("login", path="/stuseven/sevenlogin/")
        return HttpResponse("登录失败")


def deal_session_view(request):
    request.session["uname"] = "zhangsan"

    # 设置有效时间
    # request.session.set_expiry(3*24*60*60)

    # 删除session数据
    # del request.session["uname"]
    # request.session.clear()

    # 删除session对象和数据库中的数据
    # request.session.flush()

    result = getsession(request)
    print("result: {}".format(result))
    return HttpResponse("session设置成功")


def getsession(request):
    uname = request.session["uname"]
    return uname
