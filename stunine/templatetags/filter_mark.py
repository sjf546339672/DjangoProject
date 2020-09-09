# coding: utf-8
from django.template import Library

register = Library()


@register.filter
def md(value):
    """自定义过滤器"""
    import markdown
    return markdown.markdown(value)
