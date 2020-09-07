# coding: utf-8
from django.db import models


class MovieModel(models.Model):
    mid = models.AutoField(primary_key=True)
    mname = models.CharField(unique=True, max_length=100)
    mdesc = models.TextField(blank=True, null=True)
    mimg = models.CharField(max_length=120)
    mlink = models.CharField(max_length=200)

    def __str__(self):
        return "MovieModel: {},{}".format(self.mid, self.mname)

    class Meta:
        managed = False
        db_table = 'movie'
