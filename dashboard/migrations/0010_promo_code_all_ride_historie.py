# Generated by Django 4.1.2 on 2022-11-01 08:28

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0009_user_user_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Promo_Code',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(blank=True, max_length=70, null=True)),
                ('Promocode', models.CharField(max_length=30)),
                ('Description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='All_Ride_Historie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('otp', models.IntegerField()),
                ('Date', models.DateField()),
                ('pickup_location_lat', models.DecimalField(decimal_places=8, max_digits=40)),
                ('pickup_location_long', models.DecimalField(decimal_places=8, max_digits=40)),
                ('drop_location_lat', models.DecimalField(decimal_places=8, max_digits=40)),
                ('drop_location_long', models.DecimalField(decimal_places=8, max_digits=40)),
                ('Fare', models.IntegerField()),
                ('User_ratings', models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)])),
                ('Driver_ratings', models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)])),
                ('Cancel_Ride', models.IntegerField(null=True)),
                ('Driver_Detail', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dashboard.driver')),
                ('User_Detail', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dashboard.user')),
            ],
        ),
    ]
