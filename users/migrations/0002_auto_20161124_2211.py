# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-24 14:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adminpublisher',
            name='email',
            field=models.EmailField(blank=True, help_text='\u9009\u586b\uff0c\u7528\u4e8e\u5907\u6848', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='adminpublisher',
            name='telephone',
            field=models.CharField(blank=True, help_text='\u6216\u8bb8\u7528\u4e8e\u5907\u6848\u5b58\u6863\u7684\u4fe1\u606f', max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='department',
            name='telephone',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='picture',
            field=models.CharField(blank=True, help_text='\u533b\u751f\u7167\u7247\uff0c\u5b58\u8def\u5f84', max_length=90, null=True),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='speciality',
            field=models.CharField(blank=True, help_text='\u4e3b\u6cbb\u7279\u957f', max_length=90, null=True),
        ),
        migrations.AlterField(
            model_name='hospital',
            name='level',
            field=models.CharField(choices=[('0', '\u4e00\u7ea7\u4e19\u7b49'), ('1', '\u4e00\u7ea7\u4e59\u7b49'), ('2', '\u4e00\u7ea7\u7532\u7b49'), ('3', '\u4e8c\u7ea7\u4e19\u7b49'), ('4', '\u4e8c\u7ea7\u4e59\u7b49'), ('5', '\u4e8c\u7ea7\u7532\u7b49'), ('6', '\u4e09\u7ea7\u4e19\u7b49'), ('7', '\u4e09\u7ea7\u4e59\u7b49'), ('8', '\u4e09\u7ea7\u7532\u7b49'), ('9', '\u4e09\u7ea7\u7279\u7b49')], max_length=20),
        ),
        migrations.AlterField(
            model_name='hospital',
            name='picture',
            field=models.CharField(blank=True, help_text='\u533b\u9662\u7167\u7247\uff0c\u5b58\u8def\u5f84', max_length=90, null=True),
        ),
        migrations.AlterField(
            model_name='hospital',
            name='telephone',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='hospital',
            name='type',
            field=models.CharField(blank=True, choices=[('0', '\u666e\u901a'), ('1', '\u4e13\u79d1')], help_text='\u533b\u7597\u670d\u52a1\u662f\u5426\u4e13\u79d1', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='province',
            field=models.CharField(blank=True, help_text='\u7701/\u81ea\u6cbb\u533a(\u76f4\u8f96\u5e02\u548c\u7279\u522b\u884c\u653f\u533a\u7559\u767d', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='street',
            field=models.CharField(blank=True, help_text='\u8857\u9053\u5730\u5740\u95e8\u724c\u53f7', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='credit',
            field=models.CharField(choices=[('3', 'A'), ('2', 'B'), ('1', 'C'), ('0', 'X')], help_text='\u4fe1\u7528\u989d\u5ea6', max_length=1),
        ),
        migrations.AlterField(
            model_name='patient',
            name='gender',
            field=models.CharField(choices=[('0', '\u7537'), ('1', '\u5973')], max_length=1),
        ),
    ]
