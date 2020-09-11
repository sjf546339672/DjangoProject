from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from .alipay import *


def IndexView(request):
    return render(request, "tweindex.html")


alipay = AliPay(appid="2021000117601490",
                app_notify_url="127.0.0.1:9005/stutwelve/checkPay/",
                app_private_key_path="stutwelve/keys/my_private_key.txt",
                alipay_public_key_path="stutwelve/keys/my_public_key.txt",
                return_url="127.0.0.1:9005/stutwelve/checkPay/",
                debug=True)


def ToPayView(request):
    """获取二维码支付界面"""
    m = request.POST.get("m", 12)
    import uuid

    # 获取扫码支付的请求参数
    params = alipay.direct_pay(subject="京东超市",
                               out_trade_no=uuid.uuid4().hex,
                               total_amount=str(m))
    # 获取扫码支付的请求地址
    url = alipay.gateway+"?"+params
    return HttpResponseRedirect(url)


def checkPayView(request):
    """校验是否支付完成"""
    # 获取所有请求参数
    params = request.GET.dict()

    # 移除并获取sign参数的值
    sign = params.pop('sign')

    # 校验是否支付成功
    if alipay.verify(params, sign):
        return HttpResponse('支付成功！')
    return HttpResponse('支付失败！')


























