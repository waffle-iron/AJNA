# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-05 00:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('busca', '0005_auto_20170705_0037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conteinerescaneado',
            name='codigoplano',
            field=models.BinaryField(max_length=1000),
        ),
    ]