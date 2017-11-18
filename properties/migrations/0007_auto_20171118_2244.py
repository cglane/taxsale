# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-18 22:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0006_auto_20171118_2239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='bedrooms',
            field=models.PositiveSmallIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='census_tract',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='properties.CensusTract'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='property',
            name='constructed_year',
            field=models.PositiveSmallIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='finished_sq_feet',
            field=models.PositiveSmallIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='highest_sales_price',
            field=models.DecimalField(decimal_places=2, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='lat',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='lng',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='min_bid',
            field=models.DecimalField(decimal_places=2, max_digits=20, null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='owner_address',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='property_class_code',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='property_value',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='zip_code',
            field=models.CharField(max_length=10, null=True),
        ),
    ]