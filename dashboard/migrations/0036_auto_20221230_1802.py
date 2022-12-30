# Generated by Django 3.2.9 on 2022-12-30 12:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0035_saved_destination'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='driver',
            name='earnings',
        ),
        migrations.CreateModel(
            name='Earning',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('earnings', models.IntegerField()),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.driver')),
            ],
        ),
    ]