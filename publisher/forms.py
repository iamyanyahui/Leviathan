# -*- coding: utf-8 -*-
from django import forms
from . import utils


# Forms
class LoginForm(forms.Form):
    loginname=forms.CharField(min_length=4, label='用户名')
    password = forms.CharField(min_length=4, label='密码', widget=forms.PasswordInput())


class RegisterForm(forms.Form):
    loginname = forms.CharField(required=True, min_length=4, label='管理员登录名')
    password = forms.CharField(required=True, min_length=4, label='密码',widget=forms.PasswordInput())
    second_password = forms.CharField(required=True, min_length=4, label='再次输入密码',widget=forms.PasswordInput())
    telephone = forms.CharField(required=False, label='手机号(选填)')
    email = forms.EmailField(required=False, label='邮箱(选填)',widget=forms.EmailInput())
    hospital = forms.ChoiceField(required=True, label='所属医院', widget=forms.Select(),
                                 choices=utils.select_hospital())


class BulletinForm(forms.Form):
    fee = forms.DecimalField(required=True,label='预约费用')
    available_time = forms.CharField(required=True, min_length=4,label='可预约时间')
    count_available = forms.IntegerField(required=True, label='可预约人数')
    count_occupied = forms.IntegerField(required=True, label='已预约人数')
    department = forms.ChoiceField(required=True, label='医生所属科室', widget=forms.Select(),
                                   choices=utils.getDepartments())
    doctor = forms.ChoiceField(required=True, label='医生实名', widget=forms.Select(),
                               choices=utils.getDoctors())


# class BulletinForm(forms.Form):
#     fee = forms.DecimalField(required=True, label='预约费用')
#     available_time = forms.CharField(required=True, min_length=4, label='可预约时间')
#     count_available = forms.IntegerField(required=True, label='可预约人数')
#     count_occupied = forms.IntegerField(required=True, label='已预约人数')
#     department = forms.ChoiceField(required=True, label='医生所属科室', widget=forms.Select())
#     doctor = forms.ChoiceField(required=True, label='医生实名', widget=forms.Select())
#
#     def __init__(self, *args, **kwargs):  # 执行父类的构造方法
#         hospital_id = kwargs['hospital_id']
#         kwargs.pop('hospital_id')
#
#         super(BulletinForm, self).__init__(*args, **kwargs)
#         self.fields['department'].widget.choices = utils.getDepartments(hospital_id)
#         self.fields['doctor'].widget.choices = utils.getDoctors(hospital_id)
#
#         print 'department choices:'
#         print self.fields['department'].widget.choices
#         print 'doctor choices:'
#         print self.fields['doctor'].widget.choices
#         print 'args:'
#         print args
#         print '\n'


class FileForm(forms.Form):
    filefield = forms.FileField(required=True, label='请选择文件')
    # filepath = forms.FilePathField(required=True, label='请选择文件路径')
