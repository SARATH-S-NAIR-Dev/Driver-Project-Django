# Generated by Django 3.2.8 on 2021-11-19 16:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BasicEntry', '0007_drivehours'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='DriveHours',
            new_name='DriveHour',
        ),
    ]
