from django.db import models


class Clazz(models.Model):
    cname = models.CharField(max_length=30)


class Student(models.Model):
    sname = models.CharField(max_length=30)
    score = models.PositiveIntegerField()
    cls = models.ForeignKey(Clazz, on_delete=models.CASCADE)

    def __str__(self):
        return u"Student: {},{}".format(self.sname, self.score)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        try:
            self.cls = Clazz.objects.get(cname=self.cls.cname)
        except Clazz.DoesNotExist:
            self.cls = Clazz.objects.create(cname=self.cls.cname)
        models.Model.save(self, force_insert=False, force_update=False,
                          using=None,
                          update_fields=None)
#


