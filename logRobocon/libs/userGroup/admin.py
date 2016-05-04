# -*- coding: utf-8 -*-
# @Author: Macpotty
# @Date:   2016-05-04 21:02:20
# @Last Modified by:   Macpotty
# @Last Modified time: 2016-05-04 21:08:38
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from logRobocon.libs.userGroup.models import Member

class