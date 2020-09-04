from django.http import HttpResponse
from django.shortcuts import render

from student.models import StudentModel


def index(request):
    return HttpResponse("1111111")


def register(request):
    method = request.method
    if method == "GET":
        return render(request, "register.html")
    else:
        sname = request.POST.get("username", "")
        spwd = request.POST.get("password", "")
        if sname and spwd:
            stu = StudentModel(sname=sname, spwd=spwd)
            stu.save()
            return HttpResponse("注册成功")
        return HttpResponse("注册失败")


def show_view(request):
    students = StudentModel.objects.all()
    return render(request, "show.html", {"students": students})


def login_view(request):
    if request.method == "GET":
        return render(request, "login.html")
    else:
        username = request.POST.get("username")
        password = request.POST.get("password")
        if username and password:
            number = StudentModel.objects.filter(sname=username, spwd=password).count()
            if number == 1:
                return HttpResponse("登录成功")
        return HttpResponse("登陆失败")
