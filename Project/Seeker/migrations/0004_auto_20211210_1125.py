# Generated by Django 3.2.8 on 2021-12-10 05:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Seeker', '0003_seekerprofilelongdrive_seekerprofilepackage_seekerprofileshortdrive'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='seekerprofilelongdrive',
            name='LongDriveVehicleType',
        ),
        migrations.RemoveField(
            model_name='seekerprofilepackage',
            name='PackageVehicleType',
        ),
        migrations.RemoveField(
            model_name='seekerprofileshortdrive',
            name='ShortDriveVehicleType',
        ),
    ]
