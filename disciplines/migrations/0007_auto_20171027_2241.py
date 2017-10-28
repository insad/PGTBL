# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-28 00:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('disciplines', '0006_discipline_is_closed'),
    ]

    operations = [
        migrations.AddField(
            model_name='discipline',
            name='monitors_limit',
            field=models.PositiveIntegerField(default=0, help_text='Monitors limit to insert in the class.', verbose_name='Monitors limit'),
        ),
        migrations.AlterField(
            model_name='discipline',
            name='student_limit',
            field=models.PositiveIntegerField(default=0, help_text='Students limit to get in the class.', verbose_name='Students limit'),
        ),
    ]
