# -*- coding: utf-8 -*-
# @Author: Macpotty
# @Date:   2016-04-28 03:47:19
# @Last Modified by:   Macpotty
# @Last Modified time: 2016-05-05 20:45:25
from django.conf.urls import url
from logRobocon.apps.blog import views

urlpatterns = [
    url(r'^$', views.login, name='login'),
    url(r'^login/$', views.login, name='login'),
    url(r'^register/$', views.register, name='register'),
    url(r'^index/$', views.index, name='index'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^changePasswd/$', views.changePasswd, name='changePasswd'),
]
