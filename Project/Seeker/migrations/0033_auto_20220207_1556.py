# Generated by Django 3.2.10 on 2022-02-07 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Seeker', '0032_remove_shortdriverbooking_shortdrivebookingduration'),
    ]

    operations = [
        migrations.AddField(
            model_name='shortdriverbooking',
            name='ShortDriveVehicleModel',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='shortdriverbooking',
            name='ShortDrivePurpose',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
