���ӵ�ַ: https://www.bilibili.com/video/BV1i7411e7CY?p=11

���
�����ݿ�����ɵ�ģ�͵���
1. python manage.py inspectdb>movie/models.py

2. def showsql():
...     print(connection.queries[-1]["sql"])

3. ģ��.object.raw("ԭ��SQL���")

4. ��ʾ���ݿ�ͼƬ�ķ���
from django.views.static import serve
if DEBUG:
    urlpatterns.append(url(r'^media/(?P<path>.*)/$', serve, {'document_root': MEDIA_ROOT}))

5. ����ͼƬ
img_path = os.path.join(os.getcwd(), "media", photo.replace("/", "\\"))
    with open(img_path, 'rb') as fp:
        response = HttpResponse(fp.read())
        response["Content-Type"] = "image/jpg"  # ��ʾ���������е�ý��������Ϣ
        response["Content-Disposition"] = "attachment;filename={}".format(img_name)
        ��HTTP�����У���һ������������inline��Ĭ��ֵ����ʾ�ظ��е���Ϣ�����ҳ���һ���ֻ�������ҳ�����ʽչʾ����
        ������attachment����ζ����Ϣ��Ӧ�ñ����ص����أ����������������һ��������Ϊ���ĶԻ��򣬽�filename��ֵ
        Ԥ��Ϊ���غ���ļ��������������ڵĻ�����
        Content-Disposition: inline
        Content-Disposition: attachment
        Content-Disposition: attachment; filename="filename.jpg"


ǰ��
<span class="tip"> What's your middle name?</span>
class="tip" ���������Χ��ʡ��




















































