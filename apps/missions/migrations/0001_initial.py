# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2019-05-18 05:35
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Missions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('missionId', models.IntegerField(default=1, verbose_name='项目编号')),
                ('missionName', models.CharField(blank=True, max_length=50, null=True, verbose_name='任务名称')),
                ('missionEndTime', models.DateTimeField(default=datetime.datetime.now, verbose_name='截止时间')),
                ('missionDesc', models.TextField(blank=True, max_length=200, null=True, verbose_name='任务详细要求')),
                ('missionStatus', models.BooleanField(default=0, verbose_name='任务完成状态')),
                ('missionMember', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='任务成员')),
            ],
            options={
                'verbose_name': '任务',
                'verbose_name_plural': '任务',
            },
        ),
    ]