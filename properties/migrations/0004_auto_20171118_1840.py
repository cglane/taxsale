# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-18 18:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0003_auto_20171118_1827'),
    ]

    operations = [
        migrations.RenameField(
            model_name='censustract',
            old_name='number',
            new_name='black_total',
        ),
        migrations.RemoveField(
            model_name='censustract',
            name='percent_black',
        ),
        migrations.RemoveField(
            model_name='censustract',
            name='percent_white',
        ),
        migrations.AddField(
            model_name='censustract',
            name='county',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='censustract',
            name='population_total',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='censustract',
            name='state',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='censustract',
            name='tract_number',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='censustract',
            name='white_total',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
