# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2019-03-25 21:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('juries', '0002_userinfo_scaleable_explanation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userinfo',
            name='scaleable_action_content',
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='scaleable_action_user',
        ),
        migrations.AddField(
            model_name='userinfo',
            name='scaleable_content_delete',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='scaleable_content_report',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='scaleable_content_unlist',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='scaleable_user_ban',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='scaleable_user_permaban',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='scaleable_user_warn',
            field=models.BooleanField(default=False),
        ),
    ]