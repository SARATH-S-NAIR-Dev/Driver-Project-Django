# Generated by Django 3.2.8 on 2021-11-19 16:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BasicEntry', '0005_rename_weekdays_weekday'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='DriveType',
            new_name='DriveMode',
        ),
        migrations.RenameField(
            model_name='drivemode',
            old_name='DriveTypes',
            new_name='DriveModes',
        ),
    ]