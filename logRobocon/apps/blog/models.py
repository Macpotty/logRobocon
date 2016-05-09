# -*- coding: utf-8 -*-
# @Author: Macpotty
# @Date:   2016-05-03 17:45:09
# @Last Modified by:   Macpotty
# @Last Modified time: 2016-05-10 03:36:46
from django.db import models
from django.contrib import admin


class Blogpost(models.Model):
    logTime = models.DateTimeField()
    logStatus = models.CharField(max_length=50)
    realName = models.CharField(max_length=20)
    logContent = models.TextField()
    logGeneral = models.CharField(max_length=10)


class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('logTime', 'logStatus', 'realName')

admin.site.register(Blogpost, BlogPostAdmin)
