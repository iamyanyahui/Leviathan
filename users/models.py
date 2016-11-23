# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.

# CREATE TABLE `patient` (
#   `id_patient` int(11) NOT NULL AUTO_INCREMENT,
#   `username` char(15) NOT NULL COMMENT '用户名，用于登陆',
#   `password` varchar(32) NOT NULL,
#   `telephone` char(15) NOT NULL COMMENT '选填，或用于备案',
#   `email` varchar(50) DEFAULT NULL COMMENT '选填，或用于备案',
#   `name` varchar(45) NOT NULL COMMENT '认证实名',
#   `credit` enum('A','B','C','X') NOT NULL COMMENT '信用额度',
#   `idcardnumber` char(18) NOT NULL COMMENT '身份证号定长18位',
#   `gender` enum('男','女') DEFAULT NULL,
#   `age` int(3) DEFAULT '0',
#   `_createtime` timestamp NULL DEFAULT CURRENT_TIMESTAMP COMMENT '注册时间',
#   PRIMARY KEY (`id_patient`),
#   UNIQUE KEY `idcardnumber_UNIQUE` (`idcardnumber`)
# ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='[患者]//"账户"';

class Patient(models.Model):
    id_patient = models.AutoField(null=False, primary_key=True, max_length=11)
    username = models.CharField(null=False, unique=True,max_length=15, help_text='用户名，用于登陆')
    password = models.CharField(null=False, max_length=32,)
    telephone = models.CharField(null=False, blank=True, max_length=15, help_text='选填，用于备案')
    email = models.EmailField(help_text='选填，用于备案', max_length=15)
    name = models.CharField(null=False, max_length=45, help_text='认证实名')
    CREDIT_LEVEL = (
        (3, 'A'),
        (2, 'B'),
        (1, 'C'),
        (0, 'X')
    )
    credit = models.CharField(null=False, choices=CREDIT_LEVEL, help_text='信用额度', max_length=1)
    idcardnumber = models.CharField(null=False, max_length=18, unique=True, help_text='身份证号定长18位')
    GENDER = (
        (0, '男'),
        (1, '女')
    )
    gender = models.CharField(null=False, choices=GENDER, max_length=1)
    age = models.IntegerField(null=False, default=0)
    _createtime = models.CharField(help_text='注册时间', max_length=100)

    # change table name, remove prefix 'users'
    class Meta:
        db_table = 'patient'

    # tostring
    def __str__(self):
        return 'username: %s id: %s' % (self.username, self.id_patient)


# CREATE TABLE `location` (
#   `id_location` int(11) NOT NULL AUTO_INCREMENT,
#   `province` varchar(20) DEFAULT NULL COMMENT '省/自治区(直辖市和特别行政区留白)',
#   `city` varchar(20) NOT NULL COMMENT '市',
#   `county` varchar(20) NOT NULL COMMENT '主城区/县',
#   `street` varchar(50) DEFAULT NULL COMMENT '街道地址门牌号',
#   PRIMARY KEY (`id_location`)
# ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='{地址}(=>[医院])';
class Location(models.Model):
    id_location = models.AutoField(null=False, primary_key=True, max_length=11)
    province = models.CharField(null=True, max_length=20, help_text='省/自治区(直辖市和特别行政区留白')
    city = models.CharField(null=False, max_length=20, help_text='市')
    county = models.CharField(null=False, max_length=20, help_text='主城区/县')
    street = models.CharField(null=True, max_length=50, help_text='街道地址门牌号')

    def __str__(self):
        return 'province: %s  city: %s  street: %s' % (self.province, self.city, self.street)

    class Meta:
        db_table = 'location'


# CREATE TABLE `hospital` (
#   `id_hospital` int(11) NOT NULL AUTO_INCREMENT,
#   `id_location` int(11) NOT NULL,
#   `name` varchar(45) NOT NULL,
#   `level` enum('三级特等','三级甲等','三级乙等','三级丙等','二级甲等','二级乙等','二级丙等','一级甲等','一级乙等','一级丙等') DEFAULT NULL,
#   `type` enum('普通','专科') DEFAULT NULL COMMENT '医疗服务是否专科',
#   `information` text,
#   `telephone` char(15) DEFAULT NULL,
#   `picture` varchar(90) DEFAULT NULL COMMENT '医院照片，存路径',
#   `_createtime` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
#   PRIMARY KEY (`id_hospital`),
#   UNIQUE KEY `name_UNIQUE` (`name`),
#   KEY `fk_hospital_location_idx` (`id_location`),
#   CONSTRAINT `fk_hospital_location` FOREIGN KEY (`id_location`) REFERENCES `location` (`id_location`) ON DELETE NO ACTION ON UPDATE NO ACTION
# ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='[医院]<={地址}';
class Hospital(models.Model):
    id_hospital = models.AutoField(null=False, primary_key=True, max_length=11)
    # todo
    id_location = models.ForeignKey(Location, on_delete=models.CASCADE)
    name = models.CharField(null=False, max_length=45)
    LEVEL = (
        (0, '一级丙等'), (1, '一级乙等'), (2, '一级甲等'), (3, '二级丙等'), (4, '二级乙等'),
        (5, '二级甲等'), (6, '三级丙等'), (7, '三级乙等'), (8, '三级甲等'), (9, '三级特等')
    )
    level = models.CharField(null=False, choices=LEVEL, max_length=20)
    TYPE = (
        (0, '普通'), (1, '专科')
    )
    type = models.CharField(null=True, choices=TYPE, max_length=20, help_text='医疗服务是否专科')
    information = models.TextField()
    telephone = models.CharField(null=True, max_length=15)
    picture = models.CharField(null=True, max_length=90, help_text='医院照片，存路径')
    _createtime = models.CharField(max_length=20)

    def __str__(self):
        return 'name: %s  level: %s' % (self.name, self.level)

    class Meta:
        db_table = 'hospital'
