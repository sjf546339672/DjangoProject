from django.http import HttpResponse
from django.shortcuts import render


def index_view(request):
    return HttpResponse("1111")


def query1_view(request, year, month):
    return HttpResponse("hello_{}_{}".format(year, month))


def query2_view(request, month, year, name):
    return HttpResponse("hello_{}_{}_{}".format(year, month, name))
