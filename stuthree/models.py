from django.db import models
from django.db.models import Manager


class GetTrueManager(Manager):
    """实现自动以逻辑修改"""
    def all(self):
        return Manager.all(self).filter(isdelete=True)


class GetFalseManager(Manager):
    """实现自动以逻辑修改"""
    def all(self):
        return Manager.all(self).filter(isdelete=False)


class BatchDelManager(Manager):
    """实现自定义逻辑删除"""

    def get_queryset(self):
        return Manager.get_queryset(self).filter(isdelete=False)

    def filter(self, *args, **kwargs):
        delList = Manager.get_queryset(self)

        def set_delete(del_queryset):
            for i in del_queryset:
                i.isdelete = True
                i.save()
        import types  # python3, 在python2中使用的new模块
        """
        python2 
        import new
        delList.delete = new.instancemethos(set_delete, delList, QuerySet)
        return delList
        """
        # python3
        delList.delete = types.MethodType(set_delete, delList)
        return delList


class StudentModel(models.Model):
    sname = models.CharField(max_length=30)
    isdelete = models.BooleanField(default=False)

    def __str__(self):
        return u"StudentModel: {}".format(self.isdelete)

    objects = BatchDelManager()

