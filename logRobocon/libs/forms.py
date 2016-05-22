# -*- coding: utf-8 -*-
# @Author: Macpotty
# @Date:   2016-05-04 21:34:29
# @Last Modified by:   Macpotty
# @Last Modified time: 2016-05-22 17:52:10
from logRobocon.libs.formsModel import *
from ckeditor.fields import RichTextFormField


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
    password = forms.CharField(max_length=50,
                               required=True,
                               error_messages={'required': '请输入密码'},
                               widget=PasswordInputWidget(attrs={'placeholder': 'Password', 'id': 'registOrigin'}))
    verifyPasswd = forms.CharField(max_length=50,
                                   required=True,
                                   widget=PasswordInputWidget(attrs={'placeholder': 'verify Password', 'id': 'registVerify'}))
    realName = forms.CharField(max_length=50,
                               required=True,
                               widget=TextInputWidget(attrs={'placeholder': 'Real Name'}))
    emailAddr = forms.EmailField(max_length=50,
                                 required=True,
                                 widget=EmailInputWidget(attrs={'placeholder': 'Email'}))


class ChangePasswdForm(forms.Form):
    oldPasswd = forms.CharField(max_length=50,
                                required=True,
                                error_messages={'required': '请输入密码'},
                                widget=PasswordInputWidget(attrs={'placeholder': 'old Password'}))
    newPasswd = forms.CharField(max_length=50,
                                required=True,
                                error_messages={'required': '请输入密码'},
                                widget=PasswordInputWidget(attrs={'placeholder': 'new Password', 'id': 'changeOrigin'}))
    verifyNewPasswd = forms.CharField(max_length=50,
                                      required=True,
                                      widget=PasswordInputWidget(attrs={'placeholder': 'verify new Password', 'id': 'changeVerify'}))


class ModifyAccountForm(forms.Form):
    emailAddr = forms.EmailField(max_length=50,
                                 required=True,
                                 widget=EmailInputWidget(attrs={'placeholder': 'Email'}))
    realName = forms.CharField(max_length=50,
                               required=True,
                               widget=TextInputWidget(attrs={'placeholder': 'Real Name'}))


class LogEditForm(forms.Form):
    logTime = forms.DateTimeField(label=u"日期时间",
                                  required=True,
                                  widget=TextInputWidget(attrs={'id': 'logTime'}))
    logStatus = forms.CharField(label=u"状态",
                                max_length=50,
                                required=True,
                                widget=TextInputWidget(attrs={'id': 'logStatus'}))
    realName = forms.CharField(label=u"提交人",
                               max_length=50,
                               required=True,
                               widget=TextInputWidget(attrs={'id': 'realName'}))
    logContent = RichTextFormField(label=u"日志正文",
                                   required=True,
                                   widget=TextAreaWidget(attrs={'id': 'logContent'}))
    formState = forms.CharField(max_length=50,
                                widget=forms.HiddenInput)
    CHOICES = (('success', '成功',), ('warning', '存在问题',), ('danger', '失败',))
    logGeneral = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)
