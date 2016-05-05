# -*- coding: utf-8 -*-
# @Author: Macpotty
# @Date:   2016-05-04 21:07:28
# @Last Modified by:   Macpotty
# @Last Modified time: 2016-05-05 22:40:25
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template.context import RequestContext
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db.utils import IntegrityError
from logRobocon.libs.forms import *


def register(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/blog/index', RequestContext(request))
    elif request.method == 'POST':
        userForm = RegistForm(request.POST)
        if userForm.is_valid():
            username = request.POST.get('username', '')
            first_name = request.POST.get('realName', '')[0]
            last_name = request.POST.get('realName', '')[1:]
            emailAddr = request.POST.get('emailAddr', '')
            password = request.POST.get('password', '')
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
            return HttpResponseRedirect('/blog/login')
    else:
        userForm = RegistForm()
    return render_to_response('register.html',
                              {'userForm': userForm},
                              context_instance=RequestContext(request))


def login(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/blog/index', RequestContext(request))
    elif request.method == 'POST':
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


@login_required()
def changePasswd(request):
    if request.method == 'POST':
        form = ChangePasswdForm(request.POST)
        if form.is_valid():
            username = request.user.username
            oldPasswd = request.POST.get('oldPasswd', '')
            user = auth.authenticate(username=username, password=oldPasswd)
            if user is not None and user.is_active:
                newPasswd = request.POST.get('newPasswd', '')
                user.set_password(newPasswd)
                user.save()
                auth.update_session_auth_hash(request, user)
                return HttpResponseRedirect('/blog/index', RequestContext(request))
            else:
                return render_to_response('changePasswd.html',
                                          RequestContext(request,
                                                         {'form': form,
                                                          'password_is_wrong': True}))
    else:
        form = ChangePasswdForm()
    return render_to_response('changePasswd.html',
                              RequestContext(request, {'form': form}))


@login_required()
def modifyAccount(request):
    if request.method == 'POST':
        form = ModifyAccountForm(request.POST)
        user = request.user
        if form.is_valid():
            first_name = request.POST.get('realName', '')[0]
            last_name = request.POST.get('realName', '')[1:]
            emailAddr = request.POST.get('emailAddr', '')
            user.set_first_name(first_name)
            user.set_last_name(last_name)
            user.set_email(emailAddr)
            return HttpResponseRedirect('/blog/index', RequestContext(request))
    else:
        form = ChangePasswdForm()
    return render_to_response('changePasswd.html',
                              RequestContext(request, {'form': form}))
