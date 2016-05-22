# -*- coding: utf-8 -*-
# @Author: Macpotty
# @Date:   2016-05-22 16:34:02
# @Last Modified by:   Macpotty
# @Last Modified time: 2016-05-22 17:00:10
from markdown import markdown
from django import template
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe


register = template.Library()


@register.filter(is_safe=True)
@stringfilter
def markdownFilter(value):
    extensions = ["nl2br", ]
    return mark_safe(markdown(value,
                              extensions,
                              safe_mode=True,
                              enable_attributes=False))
