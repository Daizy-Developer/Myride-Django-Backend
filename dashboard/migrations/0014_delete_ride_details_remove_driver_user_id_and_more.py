# Generated by Django 4.1.2 on 2022-11-09 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0013_all_ride_historie_km_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Ride_Details',
        ),
        migrations.RemoveField(
            model_name='driver',
            name='User_Id',
        ),
        migrations.RemoveField(
            model_name='driver',
            name='all_rides',
        ),
        migrations.RemoveField(
            model_name='user',
            name='User_Id',
        ),
        migrations.RemoveField(
            model_name='user',
            name='all_rides',
        ),
        migrations.AddField(
            model_name='driver',
            name='total_rides',
            field=models.IntegerField(default=1, max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='total_rides',
            field=models.IntegerField(default=0, max_length=1000),
            preserve_default=False,
        ),
    ]
