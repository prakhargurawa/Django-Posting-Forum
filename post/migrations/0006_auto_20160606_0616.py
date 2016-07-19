# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-06-06 06:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0005_auto_20160606_0606'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='height_field',
        ),
        migrations.RemoveField(
            model_name='post',
            name='width_field',
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to=b''),
        ),
    ]
