from django.core.cache import caches
from django.http import HttpResponse
from django.shortcuts import render

from stueleven.models import Clazz

# 获取缓存对象
cacheobj = caches["default"]


def cache_wrapper(func):
    def _wrapper(request, *args, **kwargs):
        # 从缓存中获取数据
        data = cacheobj.get(request.path)
        # 判断数据是否存在缓存中
        if data:
            print("读取缓存中数据")
            return HttpResponse(data)
        # 执行views函数去数据库中获取数据
        print("从数据库中获取数据")
        response = func(request, *args, **kwargs)

        print("进行缓存数据")
        # 将数据库从查询到的数据存入缓存中
        cacheobj.set(request.path, response.content)
        return response
    return _wrapper


@cache_wrapper
def eleven_index(request):
    c_list = Clazz.objects.all()
    return render(request, "elevenindex.html", {"c_list": c_list})
