# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2019-03-29 02:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('juries', '0007_auto_20190326_0655'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='confidence',
            field=models.TextField(null=True),
        ),
    ]