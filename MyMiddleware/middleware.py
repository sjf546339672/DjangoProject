# coding: utf-8
from django.utils.deprecation import MiddlewareMixin


class Row1(MiddlewareMixin):

    def process_request(self, request):
        print("中间件{}".format(1))

    def process_view(self, request, view_func, view_func_args, view_func_kwargs):
        print("中间件{}view".format(1))

    def process_response(self, request, response):
        print("中间件{}返回".format(1))
        return response


class Row2(MiddlewareMixin):

    def process_request(self, request):
        print("中间件{}".format(2))

    def process_view(self, request, view_func, view_func_args, view_func_kwargs):
        print("中间件{}view".format(2))

    def process_response(self, request, response):
        print("中间件{}返回".format(2))
        return response


class Row3(MiddlewareMixin):

    def process_request(self, request):
        print("中间件{}".format(3))

    def process_view(self, request, view_func, view_func_args, view_func_kwargs):
        print("中间件{}view".format(3))

    def process_response(self, request, response):
        print("中间件{}返回".format(3))
        return response
