# Generated by Django 4.1.4 on 2022-12-24 21:54

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0032_driver_ratings'),
    ]

    operations = [
        migrations.AddField(
            model_name='driver_offer',
            name='Address',
            field=models.CharField(default=1, max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='driver_offer',
            name='Drop_Address',
            field=models.CharField(default=1, max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='driver_offer',
            name='ratings',
            field=models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)]),
        ),
    ]