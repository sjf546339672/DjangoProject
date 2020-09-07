链接地址: https://www.bilibili.com/video/BV1i7411e7CY?p=11

后端
将数据库表生成到模型当中
1. python manage.py inspectdb>movie/models.py

2. def showsql():
...     print(connection.queries[-1]["sql"])

3. 模型.object.raw("原生SQL语句")

4. 显示数据库图片的方法
from django.views.static import serve
if DEBUG:
    urlpatterns.append(url(r'^media/(?P<path>.*)/$', serve, {'document_root': MEDIA_ROOT}))

5. 下载图片
img_path = os.path.join(os.getcwd(), "media", photo.replace("/", "\\"))
    with open(img_path, 'rb') as fp:
        response = HttpResponse(fp.read())
        response["Content-Type"] = "image/jpg"  # 表示具体请求中的媒体类型信息
        response["Content-Disposition"] = "attachment;filename={}".format(img_name)
        在HTTP场景中，第一个参数或者是inline（默认值，表示回复中的消息体会以页面的一部分或者整个页面的形式展示），
        或者是attachment（意味着消息体应该被下载到本地；大多数浏览器会呈现一个“保存为”的对话框，将filename的值
        预填为下载后的文件名，假如它存在的话）。
        Content-Disposition: inline
        Content-Disposition: attachment
        Content-Disposition: attachment; filename="filename.jpg"


前端
<span class="tip"> What's your middle name?</span>
class="tip" 超出这个范围就省略




















































