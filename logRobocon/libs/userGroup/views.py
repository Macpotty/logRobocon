# -*- coding: utf-8 -*-
# @Author: Macpotty
# @Date:   2016-05-04 21:07:28
# @Last Modified by:   Macpotty
# @Last Modified time: 2016-05-04 21:09:09
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import requestContext
from django import forms
from django.contrib.auth.models import User
from logRobocon.libs.formsModel import *


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50,
                               requestuired=True,
                               widget=TextInputWidget(attrs={'placeholder': '用户名'}))
    password = forms.CharField(max_length=50,
                               requestuired=True,
                               widget=PasswordInputWidget(attrs={'placeholder': 'Password'}))


class RegistForm(LoginForm):
    last_name = forms.CharField(max_length=50,
                                requestuired=True,
                                widget=TextInputWidget(attrs={'placeholder': 'Real Name'}))
    emailAddr = forms.EmailField(max_length=50,
                                 requestuired=True,
                                 widget=EmailInputWidget(attrs={'placeholder': 'Email'}))
    verifyPasswd = forms.CharField(max_length=50,
                                   requestuired=True,
                                   widget=PasswordInputWidget(attrs={'placeholder': 'Password'}))

    def is_valid(self):
        valid = super(LoginForm, self).is_valid() or self.cleaned_data['verifyPasswd'] != self.cleaned_data['password']
        if not valid:
            return is_valid


def register(request):
    if request.method == 'POST':
        userForm = RegistForm(request.POST)
        if userForm.is_valid():
            username = userForm.cleaned_data['username']
            last_name = userForm.cleaned_data['last_name']
            emailAddr = userForm.cleaned_data['emailAddr']
            password = userForm.cleaned_data['password']
            User.objects.create(username=username,
                                email=emailAddr,
                                password=password,
                                last_name=last_name,
                                )
            return HttpResponseRedirect('/userGroup/index')
    else:
        userForm = RegistForm()
    return render_to_response('register.html',
                              {'userForm': userForm},
                              context_instance=requestContext(request))


def login(request):
    if request.method == 'POST':
        userForm = LoginForm(request.POST)
        if userForm.is_valid():
            username = userForm.POST.get('username', '')
            password = userForm.POST.get('password', '')
            user = auth.authenticate(username=username, password=password)
            if User is not None and user.is_active:
                auth.login(request, user)
                return render_to_response('/userGroup/index.html', requestContext(request))
            else:
                return HttpResponseRedirect('/userGroup/login',
                                            requestContext(request, {'userForm': userForm, 'password_is_wrong': True}))
    else:
        userForm = LoginForm()
    return render_to_response('login.html',
                              requestContext(request, {'userForm': userForm}))


@login_requestuired()
def index(request):
    accountName = request.COOKIES.get('accountName', '')
    return render_to_response('index.html',
                              {'accountName': accountName})


def logout(request):
    response = HttpResponse('logout successful.')
    response.delete_cookie('accountName')
    return response
