# coding: utf-8
from django import forms
from .models import *


class LoginForm(forms.Form):
    sname = forms.CharField(max_length=30, label=u'姓名')
    spwd = forms.CharField(label=u'密码', widget=forms.PasswordInput)


class ClazzForm(forms.ModelForm):
    class Meta:
        model = Clazz
        fields = ("cname",)


class StuForm(forms.ModelForm):
    class Meta:
        model = Stu
        fields = ("sname",)



