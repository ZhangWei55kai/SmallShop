# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-12 14:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='frontuser',
            name='password',
            field=models.CharField(max_length=100),
        ),
    ]
