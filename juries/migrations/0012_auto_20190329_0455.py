# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2019-03-29 04:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('juries', '0011_auto_20190329_0331'),
    ]

    operations = [
        migrations.CreateModel(
            name='Case',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.TextField(null=True)),
                ('context', models.TextField(null=True)),
                ('violations', models.TextField(null=True)),
                ('image', models.TextField(null=True)),
                ('decision_score', models.FloatField(default=None, null=True)),
                ('decision_content_action', models.TextField(null=True)),
                ('decision_user_action', models.TextField(null=True)),
                ('decision_justification', models.TextField(null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='groupinfo',
            name='condition',
        ),
        migrations.AddField(
            model_name='groupinfo',
            name='round1',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='groupinfo',
            name='round2',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='groupinfo',
            name='round3',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='groupinfo',
            name='case1',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='case1', to='juries.Case'),
        ),
        migrations.AddField(
            model_name='groupinfo',
            name='case2',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='case2', to='juries.Case'),
        ),
        migrations.AddField(
            model_name='groupinfo',
            name='case3',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='case3', to='juries.Case'),
        ),
    ]