import os

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from stusix.models import StudentModel


def index(request):
    return render(request, "upload_img.html")


# 文件上传
def upload_img_view(request):
    if request.method == "GET":
        return render(request, "upload_img.html")
    else:
        uname = request.POST.get("uname", "")
        photo = request.FILES.get("photo", "")
        StudentModel.objects.create(sname=uname, photo=photo)
        return HttpResponse("上传成功")


# 显示图片
def show_all_view(request):
    students = StudentModel.objects.all()
    return render(request, "showimg.html", {"students": students})


def download_img_view(request):
    photo = request.GET.get("photo")
    # 获取图片文件名
    img_name = photo.split("/")[-1]
    # 开启一个流
    img_path = os.path.join(os.getcwd(), "media", photo.replace("/", "\\"))
    with open(img_path, 'rb') as fp:
        response = HttpResponse(fp.read())
        response["Content-Type"] = "image/jpg"
        response["Content-Disposition"] = "attachment;filename={}".format(img_name)
    return response
