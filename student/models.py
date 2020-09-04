from django.db import models


class StudentModel(models.Model):
    sname = models.CharField(max_length=30, unique=True)
    spwd = models.CharField(max_length=30)

    def __str__(self):
        return u"Student:{}".format(self.sname)

    class Meta:
        db_table = "student"


