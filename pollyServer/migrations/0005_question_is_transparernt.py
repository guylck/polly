# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-04-22 17:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pollyServer', '0004_choice_users_voted'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='is_transparernt',
            field=models.BooleanField(default=True, verbose_name='is transparent'),
            preserve_default=False,
        ),
    ]
