# Generated by Django 3.2.9 on 2022-12-06 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0025_alter_all_ride_historie_ride_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='all_ride_historie',
            name='Ride_Type',
            field=models.CharField(choices=[('RIDE', 'RIDE'), ('DELIVERY', 'DELIVERY')], default='RIDE', max_length=20),
        ),
    ]