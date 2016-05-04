# -*- coding: utf-8 -*-
# @Author: Macpotty
# @Date:   2016-04-28 03:47:19
# @Last Modified by:   michael
# @Last Modified time: 2016-04-29 04:05:43
from django.conf.urls import url
from logRobocon.libs.userGroup import views

urlpatterns = [
    url(r'^$', views.login, name='login'),
    url(r'^login/$', views.login, name='login'),
    url(r'^register/$', views.register, name='register'),
    url(r'^index/$', views.index, name='index'),
    url(r'^logout/$', views.logout, name='logout'),
]
