# -*- coding: utf-8 -*-
# @Author: Macpotty
# @Date:   2016-05-03 17:45:09
# @Last Modified by:   Macpotty
# @Last Modified time: 2016-05-04 21:08:24
from django.db import models
from django.contrib.auth.models import User


class Member(models.Model):
    # userName = models.CharField(max_length=20)
    # accountName = models.CharField(max_length=20)
    # emailAddr = models.EmailField(max_length=50)
    # userPasswd = models.CharField(max_length=20)
    user = models.OneToOneField(User)
    department = models.CharField(max_length=50)
