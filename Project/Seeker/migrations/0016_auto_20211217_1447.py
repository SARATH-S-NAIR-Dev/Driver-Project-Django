# Generated by Django 3.2.10 on 2021-12-17 09:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Seeker', '0015_alter_seekerprofilepackage_packagepurpose'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='seekerprofilepackage',
            name='PackageVehicleModel',
        ),
        migrations.RemoveField(
            model_name='seekerprofilepackage',
            name='PackageWorkingDays',
        ),
    ]
