# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-02 20:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agcs', '0004_auto_20171002_1941'),
    ]

    operations = [
        migrations.AddField(
            model_name='years',
            name='CGV',
            field=models.CharField(default='NA', max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='years',
            name='ENV',
            field=models.CharField(default='NA', max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='years',
            name='QUAL',
            field=models.CharField(default='NA', max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='years',
            name='SOC',
            field=models.CharField(default='NA', max_length=15),
            preserve_default=False,
        ),
    ]