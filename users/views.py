# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.http import HttpResponse
from forms import RegisterForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from . import utils

provinces = ['河北', '陕西', '辽宁', '吉林', '黑龙江', '江苏', '浙江', '安徽', '福建', '江西', '山东', '河南', '湖北', '湖南', '广东'
    , '海南', '四川', '贵州', '云南', '陕西', '甘肃', '青海', '北京', '天津', '上海', '重庆', '内蒙古', '广西', '宁夏', '新疆', '西藏']
provinces.sort()

#在需要鉴别用户身份的地方，调用request.user.is_authenticated()判断即可
# Create your views here.
def index(request):
    province = request.GET.get('province', None)
    city = request.GET.get('city', None)
    hospitals = None
    cities = None
    if city:
        hospitals = utils.getHospitals(city)
    elif province:
        cities = utils.getCities(province)
    return render(request, 'users/index.html', {'username': request.user.username, 'provinces': provinces
           , 'cities': cities, 'hospitals': hospitals})



def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if not form.is_valid():
            form = LoginForm()
            return render(request, 'users/login.html', {'form': form, 'error_message': '用户名或密码不正确'})
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                auth_login(request, user)
                return redirect('/users')
            else:
                return HttpResponse('您的账户已被禁用')
        else:
            form = LoginForm()
            return render(request, 'users/login.html', {'form': form, 'error_message': '用户名或密码不正确'})
    else:
        form = LoginForm()
        return render(request, 'users/login.html', {'form': form})


def logout(request):
    auth_logout(request)
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


def hospital(request):
    hospital_id = request.GET.get('hospital_id', None)
    return render(request, 'users/hospital.html', {'username': request.user.username,'hospital': utils.getHospital(hospital_id)})
