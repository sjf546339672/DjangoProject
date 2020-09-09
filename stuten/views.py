from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import View

from stuten.forms import LoginForm, ClazzForm, StuForm


class LoginView(View):

    def get(self, request):
        loginform = LoginForm()
        return render(request, "tenlogin.html", {"loginform": loginform})

    def post(self, request):
        loginform = LoginForm(request.POST)
        # 校验数据是否合法
        if loginform.is_valid():
            data = loginform.cleaned_data
            user = authenticate(username=data["sname"], password=data["spwd"])
            if user:
                # 将用户信息存放到session中
                login(request, user)
                return HttpResponse("登录成功")
        return HttpResponse("登录失败")


class RegisterView(View):

    def get(self, request):
        cForm = ClazzForm()
        sForm = StuForm()
        return render(request, "tenregister.html", {"clazzForm": cForm,
                                                    "stuForm": sForm})

    def post(self, request):
        # 创建表单对象
        cls_Form = ClazzForm(request.POST)
        stu_Form = StuForm(request.POST)
        if cls_Form.is_valid()*stu_Form.is_valid():
            print("=========={}{}".format(cls_Form, stu_Form))
            cls = cls_Form.save()
            stu = stu_Form.save(commit=False)  # commit事务不提交
            stu.clazz = cls
            stu.save()
            return HttpResponse("注册成功")
        return HttpResponse("注册失败")














