# -*- coding: utf-8 -*-
# @Author: Macpotty
# @Date:   2016-05-04 21:07:28
# @Last Modified by:   Macpotty
# @Last Modified time: 2016-05-05 19:53:51
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template.context import RequestContext
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db.utils import IntegrityError
from logRobocon.libs.forms import *


def register(request):
    if request.method == 'POST':
        userForm = RegistForm(request.POST)
        if userForm.is_valid():
            username = request.POST.get('username', '')
            first_name = request.POST.get('last_name', '')[0]
            last_name = request.POST.get('last_name', '')[1:]
            emailAddr = request.POST.get('emailAddr', '')
            password = request.POST.get('password', '')
            verifyPasswd = request.POST.get('verifyPasswd', '')
            try:
                User.objects.create_user(username=username,
                                         email=emailAddr,
                                         password=password,
                                         first_name=first_name,
                                         last_name=last_name,
                                         )
            except IntegrityError:
                return render_to_response('register.html',
                                          RequestContext(request,
                                                         {'userForm': userForm,
                                                          'already_in_use': True}))
            # use ajax replace it.
            if password != verifyPasswd:
                return render_to_response('register.html',
                                          RequestContext(request,
                                                         {'userForm': userForm,
                                                          'not_verified': True}))
            # use js method replace it.
            elif request.user is not None and request.user.is_active:
                return HttpResponseRedirect('/blog/logout', RequestContext(request))
            else:
                return HttpResponseRedirect('/blog/login')
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
                return render_to_response('login.html',
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
        return render_to_response('index.html')


@login_required()
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/blog/login')
