# Generated by Django 3.2.8 on 2021-11-19 06:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('BasicEntry', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='VehicleType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('VehicleTypes', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='VehicleModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ModelName', models.CharField(max_length=20)),
                ('VehicleTypes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BasicEntry.vehicletype')),
            ],
        ),
    ]
