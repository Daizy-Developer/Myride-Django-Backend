# Generated by Django 4.1.2 on 2022-11-24 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0018_remove_all_ride_historie_carpooling_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ride_offer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('User_Uid', models.CharField(max_length=100)),
                ('Driver_Uid', models.CharField(blank=True, max_length=100, null=True)),
                ('pickup_location_lat', models.DecimalField(decimal_places=8, max_digits=40)),
                ('pickup_location_long', models.DecimalField(decimal_places=8, max_digits=40)),
                ('drop_location_lat', models.DecimalField(decimal_places=8, max_digits=40)),
                ('drop_location_long', models.DecimalField(decimal_places=8, max_digits=40)),
                ('Driver_offer', models.IntegerField()),
            ],
        ),
    ]