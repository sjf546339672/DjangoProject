import math

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from movie.models import MovieModel


# 原生分页
def show_view(request):
    # 获取请求的页码
    num = request.GET.get("num", 1)
    # 处理分页
    movies, number = get_page(int(num))

    # 上一页页码
    pre_page_num = number - 1
    # 下一页页码
    next_page_num = number + 1

    return render(request, "movie.html", {"movies": movies,
                                          "pre_page_num": pre_page_num,
                                          "next_page_num": next_page_num})


# Django分页
def show_data_view(request):
    # 获取当前页码数
    num = request.GET.get("num", 1)
    num = int(num)

    # 获取数据库所有数据
    movies = MovieModel.objects.all()

    # 创建分页对象
    pagination = Paginator(movies, 20)
    # 获取当前页数据
    try:
        pre_data = pagination.page(num)
    except PageNotAnInteger: # 获取num不是int
        # 返回第一页
        pre_data = pagination.page(1)
    except EmptyPage:  # 获取的num超过总长度
        # 返回最后一页数据
        pre_data = pagination.page(pagination.num_pages)  # num_pages最后一页
    page_list = get_page_list(num, pagination)
    return render(request, "movie01.html", {"movies": pre_data,
                                            "pagination": pagination,
                                            "pagelist": page_list,
                                            "currentPage": num})


def get_page(num, size=20):
    """ 处理分页 """
    # 总记录数
    totalRecords = MovieModel.objects.count()
    # 总页数
    totalPage = int(math.ceil(totalRecords*1.0/size))

    # 判断是否越界
    if num < 1:
        num = 1
    if num > totalPage:
        num = totalPage

    # 计算每页显示的记录
    #   1     0   :    2  [0:2]
    #   2     2   :    4  [2:4]
    #   3     4   :    6  [4:6]
    #  num  size      [((num-1)*size): num*size]
    movies = MovieModel.objects.all()[((num-1)*size): num*size]
    return movies, num


def get_page_list(num, pagination):
    """分页页码变化设置"""
    # 每一页开始页码
    begin_page = (num - int(math.ceil(10.0 / 2)))
    if begin_page < 1:
        begin_page = 1
    # 每一页结束页码
    end_page = begin_page + 9
    if end_page > pagination.num_pages:
        end_page = pagination.num_pages

    if end_page < 10:
        begin_page = 1
    else:
        begin_page = end_page - 9
    page_list = range(begin_page, end_page + 1)
    return page_list

