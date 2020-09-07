from django.db import models


# Create your models here
class StudentModel(models.Model):
    sno = models.AutoField(primary_key=True)
    sname = models.CharField(max_length=30)
    photo = models.ImageField(upload_to="imgs")

    def __str__(self):
        return u"StudentModel: {}".format(self.sname)
