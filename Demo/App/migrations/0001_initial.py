# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-02-25 13:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=200)),
                ('mail', models.CharField(max_length=200)),
                ('psw', models.CharField(max_length=200)),
            ],
        ),
    ]
