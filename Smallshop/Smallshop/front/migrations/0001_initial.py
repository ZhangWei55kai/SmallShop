# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-12 14:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FrontUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=100)),
                ('points', models.IntegerField(default=0)),
                ('vipLevel', models.IntegerField(default=0)),
                ('createtime', models.DateField(auto_now_add=True)),
                ('balance', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
            ],
        ),
    ]
