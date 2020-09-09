from django.db import models

# Create your models here.


class Clazz(models.Model):
    cname = models.CharField(max_length=30)
