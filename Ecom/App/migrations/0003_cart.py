# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-03-20 13:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0002_register'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('crt_id', models.CharField(max_length=200)),
                ('crt_name', models.CharField(max_length=200)),
                ('crt_desc', models.CharField(max_length=200)),
            ],
        ),
    ]
