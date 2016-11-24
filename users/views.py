# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.http import HttpResponse
from forms import RegisterForm, LoginForm
from . import utils


# Create your views here.
def index(request):
    session = request.session
    islogin = session.get('islogin', False)
    if islogin:
        return render(request, 'users/index.html', {'username': session['username']})
    else:
        return redirect('/users/login/')


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if utils.authUser(form):
            request.session['islogin'] = True
            request.session['username'] = form.cleaned_data['username']
            request.session.set_expiry(600)
            return redirect('/users')
        else:
            form = LoginForm()
            return render(request, 'users/login.html', {'form': form, 'error_message': '用户名或密码不正确'})
    else:
        form = LoginForm()
        return render(request, 'users/login.html', {'form': form})


def logout(request):
    request.session.clear()
    return HttpResponse('注销成功')


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            if not form.cleaned_data['password'] == form.cleaned_data['second_password']:
                form = RegisterForm()
                return render(request, 'users/register.html', {'form': form, 'error_message': '两次密码输入不一致!'})
            else:
                utils.addUser(form)
                return render(request, 'users/regsuccess.html')
        else:
            form = RegisterForm()
            return render(request, 'users/register.html', {'form': form, 'error_message': '请输入正确信息!'})
    else:
        form = RegisterForm()
        return render(request, 'users/register.html', {'form': form})
