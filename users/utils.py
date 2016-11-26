# -*- coding: utf-8 -*-
# 功能函数放置在此文件中
from forms import RegisterForm, LoginForm
from django.db import models
from . import models as my_models
import datetime
import pytz
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


def getHospitals(city):
    locations=my_models.Location.objects.filter(city__contains=city)
    hospitals = []
    for location in locations:
        find=my_models.Hospital.objects.filter(id_location=location.id_location)
        for hospital in find:
            hospitals.append(hospital)
    return hospitals


def getCities(province):
    provinces=my_models.Location.objects.filter(province__contains=province)
    cities=[]
    for province in provinces:
        cities.append(province.city)
    return cities


def getBulletins(hospital_id):
    departments=my_models.Department.objects.filter(id_hospital=hospital_id)
    bulletins=[]
    for department in departments:
        doctor_department=my_models.DoctorDepartment.objects.filter(id_department=department.id_department).first()
        finds=my_models.Bulletin.objects.filter(id_doctor_department=doctor_department.id_doctor_department)
        for find in finds:
            if find.availabletime > pytz.utc.localize(datetime.datetime.now()):
                bulletins.append(find)
    return bulletins