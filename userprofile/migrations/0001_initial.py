# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-03-06 06:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=42)),
                ('email', models.EmailField(max_length=75)),
                ('updated_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
