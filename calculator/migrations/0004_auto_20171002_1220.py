# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-02 12:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculator', '0003_auto_20171002_1220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pair',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=4),
        ),
    ]
