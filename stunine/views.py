from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader, Context, Template, RequestContext
from django.views import View

from stunine.my_context_process import getData


class IndexViews(View):
    def get(self, request, *args, **kwargs):
        return render(request, "ninesubmit.html")

    def post(self, request, *args, **kwargs):
        return HttpResponse("POST请求")


class IndexViews2(View):

    def get(self, request):
        temp = loader.get_template("ninelogin.html")
        # c = Context({"name": "zhangsan"})
        str1 = temp.render({"name": "zhangsan"})
        print("==========", str1)
        return HttpResponse(str1)


class IndexViews3(View):

    def get(self, request):
        content = "### 自定义过滤器"
        return render(request, "ninemd.html", {"content": content})


class IndexViews4(View):

    def get(self, request, *args, **kwargs):
        return render(request, "niniedata.html")


class IndexViews5(View):

    def get(self, request):
        temp = Template("{{name}}")
        str1 = temp.render(RequestContext(request, dict_=None, processors=(getData, )))
        return HttpResponse(str1)
