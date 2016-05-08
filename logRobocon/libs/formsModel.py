# -*- coding: utf-8 -*-
# @Author: michael
# @Date:   2016-04-29 02:50:03
# @Last Modified by:   Macpotty
# @Last Modified time: 2016-05-08 18:22:25
from django import forms


class TextInputWidget(forms.TextInput):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('attrs', {}).update({'class': 'form-control'})
        super(TextInputWidget, self).__init__(*args, **kwargs)


class TextAreaWidget(forms.Textarea):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('attrs', {}).update({'class': 'form-control',
                                               'rows': 5})
        super(TextAreaWidget, self).__init__(*args, **kwargs)


class PasswordInputWidget(forms.PasswordInput):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('attrs', {}).update({'class': 'form-control'})
        super(PasswordInputWidget, self).__init__(*args, **kwargs)


class EmailInputWidget(forms.EmailInput):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('attrs', {}).update({'class': 'form-control'})
        super(EmailInputWidget, self).__init__(*args, **kwargs)
