# -*- coding: utf-8 -*-
# 功能函数放置在此文件中
from forms import RegisterForm, LoginForm
from django.db import models
from . import models
import datetime
from django.contrib.auth.models import User


def addUser(form):
    data = form.cleaned_data
    patient = models.Patient.objects.create(username=data['username'], password=data['password'],
                                            telephone=data['telephone']
                                            , email=data['email'], name=data['name'], credit='A', gender=data['gender'],
                                            age=data['age']
                                            , _createtime=datetime.datetime.now(), idcardnumber=data['idcardnumber'])
    patient.save()
    user = User.objects.create_user(form.cleaned_data['username'], form.cleaned_data['email'],
                                    form.cleaned_data['password'])
    user.save()


def authUser(form):
    if form.is_valid():
        data = form.cleaned_data
        username = data['username']
        password = data['password']
        # check
        user = models.Patient.objects.filter(username=username, password=password)
        if user:
            return True
        else:
            return False
    else:
        return False
