from django.db import models


# 帖子模型类
class PostModel(models.Model):
    pid = models.AutoField(primary_key=True)  # id
    title = models.CharField(max_length=120, unique=True)  # 主题
    connect = models.TextField()  # 内容
    create_time = models.DateTimeField(auto_now_add=True)  # 创建时间
    modified_time = models.DateTimeField(auto_now_add=True)  # 修改时间
    email = models.EmailField()  # email
    isdelete = models.BooleanField(default=False)  # 删除标记，删True
    access_count = models.PositiveIntegerField()  # 访问量，没有负数
    price = models.DecimalField(max_digits=5, decimal_places=2)  # 小数
    file = models.ImageField(upload_to="upload/images/")

    def __str__(self):
        return u"PostModel:{}, {}".format(self.pid, self.title, self.access_count)

    class Meta:
        db_table = "post_model"


class StudentModel(models.Model):
    sno = models.AutoField(primary_key=True)  # 学号
    sname = models.CharField(max_length=30)  # 姓名

    def __str__(self):
        return u"StudentModel: {}".format(self.sname)


class ScardModel(models.Model):
    student = models.OneToOneField(StudentModel, primary_key=True, on_delete=models.CASCADE)
    major = models.CharField(max_length=30, unique=True)  # 专业

    def __str__(self):
        return u"ScardModel: {}".format(self.major)
