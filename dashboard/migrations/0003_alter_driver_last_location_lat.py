# Generated by Django 4.0.6 on 2022-09-24 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_ride_details'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver',
            name='last_location_lat',
            field=models.DecimalField(decimal_places=2, max_digits=200),
        ),
    ]
