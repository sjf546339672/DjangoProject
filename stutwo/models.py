from django.db import models

# Create your models here.


class ClazzModel(models.Model):
    cno = models.AutoField(primary_key=True)
    cname = models.CharField(max_length=30)

    def __unicode__(self):
        return u"ClazzModel: {}".format(self.cname)


class CourseModel(models.Model):
    course_no = models.AutoField(primary_key=True)
    course_name = models.CharField(max_length=30)


class StudentModel(models.Model):
    sno = models.AutoField(primary_key=True)
    sname = models.CharField(max_length=30)
    cls = models.ForeignKey(ClazzModel, on_delete=models.CASCADE)
    cour = models.ForeignKey(CourseModel, on_delete=models.CASCADE)
