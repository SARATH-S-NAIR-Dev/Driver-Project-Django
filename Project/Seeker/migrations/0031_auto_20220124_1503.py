# Generated by Django 3.2.10 on 2022-01-24 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Seeker', '0030_alter_shortdriverbooking_shortdrivebookingdroplocation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='packagebooking',
            name='Purpose',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='packagebooking',
            name='Vehiclemodel',
            field=models.CharField(max_length=20, null=True),
        ),
    ]