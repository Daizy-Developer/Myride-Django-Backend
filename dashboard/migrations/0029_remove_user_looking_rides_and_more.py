# Generated by Django 4.1.4 on 2022-12-23 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0028_user_looking_rides'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='looking_rides',
        ),
        migrations.AlterField(
            model_name='all_ride_historie',
            name='status',
            field=models.CharField(choices=[('BOOKED', 'BOOKED'), ('ARRIVED', 'ARRIVED'), ('ARRIVING', 'ARRIVING'), ('CANCELLED', 'CANCELLED'), ('ENDED', 'ENDED'), ('ADVANCE BOOKING', 'ADVANCE BOOKING')], default='BOOKED', max_length=20),
        ),
    ]
