# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-08-28 12:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('helpline', '0010_auto_20180826_2244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='call_xform',
            field=models.ForeignKey(blank=True, help_text='Call Case Form', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='call_xform', to='logger.XForm'),
        ),
        migrations.AlterField(
            model_name='service',
            name='qa_xform',
            field=models.ForeignKey(blank=True, help_text='Quality Analysis Form', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='qa_xform', to='logger.XForm'),
        ),
        migrations.AlterField(
            model_name='service',
            name='walkin_xform',
            field=models.ForeignKey(blank=True, help_text='Walkin Case Form', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='walkin_xform', to='logger.XForm'),
        ),
        migrations.AlterField(
            model_name='service',
            name='web_online_xform',
            field=models.ForeignKey(blank=True, help_text='Quality Analysis Form', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='web_online_xform', to='logger.XForm'),
        ),
    ]
