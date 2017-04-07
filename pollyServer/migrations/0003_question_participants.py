# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-04-07 11:33
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pollyServer', '0002_auto_20170329_0148'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='participants',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]