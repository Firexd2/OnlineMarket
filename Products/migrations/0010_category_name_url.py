# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-21 16:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0009_product_weight'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='name_url',
            field=models.CharField(default='', max_length=50, verbose_name='URL категории'),
        ),
    ]
