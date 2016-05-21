# -*- coding: utf-8 -*-
# @Author: Macpotty
# @Date:   2016-05-04 21:07:28
# @Last Modified by:   Macpotty
<<<<<<< HEAD
# @Last Modified time: 2016-05-21 15:35:00
=======
# @Last Modified time: 2016-05-10 22:57:50
>>>>>>> bed3c3de3d9819841e4a31c72b1d0e098dedf387
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template.context import RequestContext
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db.utils import IntegrityError
from django.views.generic import ListView
from logRobocon.libs.forms import *
from logRobocon.apps.blog.models import Blogpost
import time


class LogList(ListView):
    context_object_name = 'logList'
    template_name = 'logList.html'
    paginate_by = 14
    model = Blogpost

    def get_context_data(self, **kwargs):
        context = super(LogList, self).get_context_data(**kwargs)
        context['username'] = self.request.user.last_name
        context['page_logList'] = True
        return context


@login_required()
def logEdit(request):
    user = request.user
    page = request.GET.get('page', '')
    if request.method == 'POST':
        logForm = LogEditForm(request.POST)
        if logForm.is_valid():
            logTime = request.POST.get('logTime', '')
            logStatus = request.POST.get('logStatus', '')
            realName = request.POST.get('realName', '')
            logContent = request.POST.get('logContent', '')
            logGeneral = request.POST.get('logGeneral', '')
            formState = request.GET.get('formState', '')
            if formState == 'create':
                Blogpost.objects.create(logTime=logTime,
                                        logStatus=logStatus,
                                        realName=realName,
                                        logContent=logContent,
                                        logGeneral=logGeneral)
            else:
                objBlog = Blogpost.objects.get(id=int(formState))
                objBlog.logTime = logTime
                objBlog.logStatus = logStatus
                objBlog.realName = realName
                objBlog.logContent = logContent
                objBlog.logGeneral = logGeneral
                objBlog.save()
            return HttpResponseRedirect('/blog/logList/?page=' + str(page))
    else:
        formState = request.GET.get('formState', '')
        if formState != 'create':
            objBlog = Blogpost.objects.get(id=int(formState))
            logForm = LogEditForm(initial={'realName': objBlog.realName,
                                           'logTime': time.strftime("%Y-%m-%d %H:%M", time.localtime(time.time())),
                                           'logStatus': objBlog.logStatus,
                                           'logContent': objBlog.logContent,
                                           'logGeneral': objBlog.logGeneral,
                                           'formState': formState})
        else:
            logForm = LogEditForm(initial={'realName': user.first_name + user.last_name,
                                           'logTime': time.strftime("%Y-%m-%d %H:%M", time.localtime(time.time())),
                                           'formState': formState})
    return render_to_response('logEdit.html',
                              RequestContext(request, {'logForm': logForm,
                                                       'username': user.last_name,
                                                       'page': page}))


@login_required()
def logDelete(request):
    logId = request.GET.get('formState', '')
    page = request.GET.get('page', '')
    objBlog = Blogpost.objects.get(id=int(logId))
    objBlog.delete()
    return HttpResponseRedirect('/blog/logList/?page=' + str(page))


@login_required()
def logShow(request):
    user = request.user
    logId = request.GET.get('logId', '')
    page = request.GET.get('page', '')
    objBlog = Blogpost.objects.get(id=int(logId))
    return render_to_response('logShow.html',
                              RequestContext(request,
                                             {'user': user,
                                              'objBlog': objBlog,
                                              'page': page}))


def register(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/blog/index', RequestContext(request))
    elif request.method == 'POST':
        userForm = RegistForm(request.POST)
        if userForm.is_valid():
            username = request.POST.get('username', '')
            realName = request.POST.get('realName', '')
            if realName[:2] == '欧阳':
                first_name = realName[:2]
                last_name = realName[2:]
            else:
                first_name = realName[0]
                last_name = realName[1:]
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
                                  RequestContext(request, {'username': request.user.last_name,
                                                           'page_index': True}))
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
    user = request.user
    if request.method == 'POST':
        user = request.user
        form = ModifyAccountForm(request.POST)
        if form.is_valid():
            first_name = request.POST.get('realName', '')[0]
            last_name = request.POST.get('realName', '')[1:]
            emailAddr = request.POST.get('emailAddr', '')
            user.first_name = first_name
            user.last_name = last_name
            user.email = emailAddr
            user.save()
            return HttpResponseRedirect('/blog/index', RequestContext(request))
    else:
        form = ModifyAccountForm(initial={'emailAddr': user.email, 'realName': user.first_name + user.last_name})
    return render_to_response('modifyAccount.html',
                              RequestContext(request, {'form': form}))


def future(request):
    return render_to_response('future.html',
                              RequestContext(request, {'username': request.user.last_name,
                                                       'page_future': True}))
