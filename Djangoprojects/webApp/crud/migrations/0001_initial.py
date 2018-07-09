# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-26 03:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_name', models.CharField(max_length=100)),
                ('emp_email', models.EmailField(max_length=100)),
                ('address', models.CharField(max_length=250)),
            ],
        ),
    ]
