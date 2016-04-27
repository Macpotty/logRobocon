from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django import forms
from models import User


class LoginForm(forms.Form):
    accountName = forms.CharField(label='用户名', max_length=50)
    userPasswd = forms.CharField(label='Password',
                                 max_length=50,
                                 wiget=forms.PasswordInput())


class RegistForm(LoginForm):
    userName = forms.CharField(label='Real Name', max_length=50)
    emailAddr = forms.EmailField(label='Email address', max_length=50)


def register(req):
    if req.method == 'POST':
        userForm = RegistForm(req.POST)
        if userForm.is_valid():
            userName = userForm.cleaned_data['userName']
            userPasswd = userForm.cleaned_data['Password']
            User.objects.create(userName=userName, userPasswd=userPasswd)
            return HttpResponse('register successful.')
    else:
        userForm = RegistForm()
    return render_to_response('register.html',
                              {'userName': userName},
                              context_instance=RequestContext(req))


def login(req):
    if req.method == 'POST':
        userForm = LoginForm(req.POST)
        if userForm.is_valid():
            userName = userForm.cleaned_data['userName']
            userPasswd = userForm.cleaned_data['Password']
            verifyValue = User.objects.filter(username_exact=userName,
                                              password_exact=userPasswd)
            if verifyValue:
                response = HttpResponseRedirect('/userGroup/index')
                response.set_cookie('userName', userName, 10800)
                return response
            else:
                return HttpResponseRedirect('/userGroup/login')
    else:
        userForm = LoginForm()
    return render_to_response('login.html',
                              {'userName': userName},
                              context_instance=RequestContext(req))


def index(req):
    userName = req.COOKIES.get('userName', '')
    return render_to_response('index.html',
                              {'userName': userName})


def logout(req):
    response = HttpResponse('logout successful.')
    response.delete_cookie('userName')
    return response
