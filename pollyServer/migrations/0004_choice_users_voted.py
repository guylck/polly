# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-04-07 20:38
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pollyServer', '0003_question_participants'),
    ]

    operations = [
        migrations.AddField(
            model_name='choice',
            name='users_voted',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
