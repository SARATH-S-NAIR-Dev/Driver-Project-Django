# Generated by Django 3.2.10 on 2021-12-21 05:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Seeker', '0022_rename_seekerlongdrive_shortdrivevehiclemodels_seekershortdrive'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shortdrivepurposes',
            old_name='SeekerPackage',
            new_name='SeekerShortDrive',
        ),
    ]
