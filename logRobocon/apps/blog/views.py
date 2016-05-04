# -*- coding: utf-8 -*-
# @Author: Macpotty
# @Date:   2016-05-04 21:07:28
# @Last Modified by:   Macpotty
# @Last Modified time: 2016-05-04 22:48:43
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template.context import RequestContext
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from logRobocon.libs.forms import *


def register(request):
    if request.method == 'POST':
        userForm = RegistForm(request.POST)
        if userForm.is_valid():
            username = request.POST.get('username', '')
            last_name = request.POST.get('last_name', '')
            emailAddr = request.POST.get('emailAddr', '')
            password = request.POST.get('password', '')
            User.objects.create_user(username=username,
                                     email=emailAddr,
                                     password=password,
                                     last_name=last_name,
                                     )
            if request.POST.get('password', '') != request.POST.get('verifyPasswd', ''):
                return HttpResponseRedirect(RequestContext(request, {'userForm': userForm, 'not_verified': True}))
            else:
                return HttpResponseRedirect('/blog/index')
    else:
        userForm = RegistForm()
    return render_to_response('register.html',
                              {'userForm': userForm},
                              context_instance=RequestContext(request))


def login(request):
    if request.method == 'POST':
        userForm = LoginForm(request.POST)
        if userForm.is_valid():
            username = request.POST.get('username', '')
            password = request.POST.get('password', '')
            user = auth.authenticate(username=username, password=password)
            if user is not None and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect('/blog/index', RequestContext(request))
            else:
                return HttpResponseRedirect('/blog/login',
                                            RequestContext(request, {'userForm': userForm, 'password_is_wrong': True}))
    else:
        userForm = LoginForm()
    return render_to_response('login.html',
                              RequestContext(request, {'userForm': userForm}))


def index(request):
    if request.user.is_authenticated():
        return render_to_response('index-after.html',
                                  RequestContext(request, {'username': request.user.last_name}))
    else:
        return render_to_response('index-before.html')


@login_required()
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/blog/login')
