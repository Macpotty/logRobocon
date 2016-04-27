# -*- coding: utf-8 -*-
# @Author: Macpotty
# @Date:   2016-04-28 03:47:19
# @Last Modified by:   Macpotty
# @Last Modified time: 2016-04-28 03:58:09
from django.conf.urls import url
from userGroup import views

urlpatterns = [
    url(r'^$', views.login, name='login'),
    url(r'^login/$', views.login, name='login'),
    url(r'^regist/$', views.regist, name='regist'),
    url(r'^index/$', views.index, name='index'),
    url(r'^logout/$', views.logout, name='logout'),
]
