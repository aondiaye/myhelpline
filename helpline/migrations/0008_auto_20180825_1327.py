# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-08-25 13:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('helpline', '0007_auto_20180825_0936'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clock',
            name='hl_service',
        ),
        migrations.AddField(
            model_name='clock',
            name='service',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='helpline.Service'),
        ),
    ]