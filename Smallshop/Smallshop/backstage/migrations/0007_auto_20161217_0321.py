# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-16 19:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0002_auto_20161212_2258'),
        ('backstage', '0006_auto_20161212_2243'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orderSerial', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('sendStatus', models.BooleanField(default=False)),
                ('reveiceStatus', models.BooleanField(default=False)),
                ('buyTime', models.DateTimeField(auto_now_add=True)),
                ('orderPrice', models.DecimalField(decimal_places=2, max_digits=12)),
                ('commodity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backstage.Commodity')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='front.FrontUser')),
            ],
        ),
        migrations.AddField(
            model_name='shoppingcart',
            name='buyNum',
            field=models.IntegerField(default=1),
        ),
    ]
