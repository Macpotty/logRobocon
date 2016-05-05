# -*- coding: utf-8 -*-
# @Author: Macpotty
# @Date:   2016-05-04 21:34:29
# @Last Modified by:   Macpotty
# @Last Modified time: 2016-05-05 18:07:39
from logRobocon.libs.formsModel import *


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50,
                               required=True,
                               error_messages={'required': '请输入用户名'},
                               widget=TextInputWidget(attrs={'placeholder': '用户名'}))
    password = forms.CharField(max_length=50,
                               required=True,
                               error_messages={'required': '请输入密码'},
                               widget=PasswordInputWidget(attrs={'placeholder': 'Password'}))


class RegistForm(LoginForm):
    verifyPasswd = forms.CharField(max_length=50,
                                   required=True,
                                   widget=PasswordInputWidget(attrs={'placeholder': 'verify Password'}))
    last_name = forms.CharField(max_length=50,
                                required=True,
                                widget=TextInputWidget(attrs={'placeholder': 'Real Name'}))
    emailAddr = forms.EmailField(max_length=50,
                                 required=True,
                                 widget=EmailInputWidget(attrs={'placeholder': 'Email'}))
