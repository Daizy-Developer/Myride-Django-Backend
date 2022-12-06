# Generated by Django 3.2.9 on 2022-12-06 14:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0026_alter_all_ride_historie_ride_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('Time', models.TimeField()),
                ('reciever', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dashboard.driver')),
                ('ride', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.all_ride_historie')),
                ('sender', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dashboard.user')),
            ],
        ),
        migrations.CreateModel(
            name='Driver_Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('Time', models.TimeField()),
                ('reciever', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dashboard.user')),
                ('ride', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.all_ride_historie')),
                ('sender', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dashboard.driver')),
            ],
        ),
    ]
