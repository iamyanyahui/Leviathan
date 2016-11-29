# -*- coding: utf-8 -*-
# 功能函数放置在此文件中
# from forms import LoginForm, RegisterForm
from django.db import models
from users import models
import datetime


def add_publisher(form):
    data = form.cleaned_data
    publisher = models.Adminpublisher.objects.create(loginname=data['loginname'],
                                            password=data['password'],
                                            telephone=data['telephone'],
                                            email=data['email'],
                                            _createtime=datetime.datetime.now(),
                                            id_hospital_id=data['hospital'])
    publisher.save()


def auth_publisher(form):
    if form.is_valid():
        data = form.cleaned_data
        loginname = data['loginname']
        password = data['password']
        # check
        publisher = models.Adminpublisher.objects.filter(loginname=loginname, password=password)
        if publisher:
            return True
        else:
            return False
    else:
        return False


def select_hospital():
    hospital = models.Hospital.objects.all().values('id_hospital', 'name')
    h_list=[]
    if hospital:
        for h_dict in hospital:
            t_tuple = (h_dict['id_hospital'], h_dict['name'])
            h_list.append(t_tuple)
    return h_list


def publisher_exists(name):
    publisher = models.Adminpublisher.objects.filter(loginname=name)
    if publisher:
        return True
    return False


def select_all_bulletin():
    bulletins = models.Bulletin.objects.all()
    return bulletins
