# Generated by Django 4.1.4 on 2022-12-23 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0029_remove_user_looking_rides_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='all_ride_historie',
            name='Address',
            field=models.CharField(default=1, max_length=500),
            preserve_default=False,
        ),
    ]