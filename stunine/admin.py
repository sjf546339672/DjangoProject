from django.contrib import admin

# Register your models here.
from stunine.models import BlogArticles


class BlogAdmin(admin.ModelAdmin):
    # 显示字段
    list_display = ("title", "author", "publish")
    # 条件查询字段
    list_filter = ("publish", "author")
    # 搜索框中根据某些字段进行查询
    search_fields = ('title', 'body')
    raw_id_fields = ('author',)
    # 以某个日期字段分层查询
    date_hierarchy = 'publish'
    # 排列字段
    ordering = ['publish', 'author']


admin.site.register(BlogArticles, BlogAdmin)
