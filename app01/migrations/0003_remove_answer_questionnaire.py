# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-04 14:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0002_answer_questionnaire'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='questionnaire',
        ),
    ]
