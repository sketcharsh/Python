# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-02-05 09:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RegisterDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usrFn', models.CharField(max_length=200)),
                ('usrLn', models.CharField(max_length=200)),
                ('usrPs', models.CharField(max_length=200)),
                ('usrPh', models.IntegerField()),
                ('usrEm', models.CharField(max_length=200)),
            ],
        ),
    ]
