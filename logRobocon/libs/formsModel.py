# -*- coding: utf-8 -*-
# @Author: michael
# @Date:   2016-04-29 02:50:03
# @Last Modified by:   michael
# @Last Modified time: 2016-04-29 03:08:21
from django import forms


class TextInputWidget(forms.TextInput):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('attrs', {}).update({'class': 'form-control'})
        super(TextInputWidget, self).__init__(*args, **kwargs)


class PasswordInputWidget(forms.PasswordInput):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('attrs', {}).update({'class': 'form-control'})
        super(PasswordInputWidget, self).__init__(*args, **kwargs)


class EmailInputWidget(forms.PasswordInput):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('attrs', {}).update({'class': 'form-control'})
        super(EmailInputWidget, self).__init__(*args, **kwargs)
