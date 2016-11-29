# coding:utf-8
from django.shortcuts import render, redirect
from django.http import HttpResponse
from forms import LoginForm, RegisterForm
from . import utils


# Create your views here.
def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if utils.auth_publisher(form):
            request.session['islogin'] = True
            request.session['loginname'] = form.cleaned_data['loginname']
            request.session.set_expiry(600)
            return redirect('/publisher')
        else:
            form = LoginForm()
            return render(request, 'publisher/login.html', {'form': form, 'error_message': '用户名或密码不正确'})
    else:
        form = LoginForm()
        return render(request, 'publisher/login.html', {'form': form})


def logout(request):
    request.session.clear()
    return HttpResponse('注销成功')


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            if not form.cleaned_data['password'] == form.cleaned_data['second_password']:
                form = RegisterForm()
                return render(request, 'publisher/register.html', {'form': form, 'error_message': '两次密码输入不一致!'})
            elif utils.publisher_exists(form.cleaned_data['loginname']):
                return render(request, 'publisher/register.html', {'form': form, 'error_message': '用户名已存在!'})
            else:
                utils.add_publisher(form)
                return render(request, 'publisher/regsuccess.html')
        else:
            form = RegisterForm()
            return render(request, 'publisher/register.html', {'form': form, 'error_message': '请输入正确信息!'})
    else:
        form = RegisterForm()
        return render(request, 'publisher/register.html', {'form': form})


def index(request):
    session = request.session
    islogin = session.get('islogin', False)
    if islogin:
        bulletins = utils.select_all_bulletin()
        return render(request, 'publisher/index.html', {'loginname': session['loginname'], 'bulletins': bulletins})
    else:
        return redirect('/publisher/login/')


#修改预约信息
def alter_bulletin(request, bulletin_id):
    pass


# 删除预约信息
def delete_bulletin(request, bulletin_id):
    pass


# 发布预约信息
def create_bulletin(request):
    pass

