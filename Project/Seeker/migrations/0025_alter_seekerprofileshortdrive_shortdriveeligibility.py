# Generated by Django 3.2.10 on 2021-12-21 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Seeker', '0024_rename_shortdrivepurposes_shortdrivepurposes_purposes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seekerprofileshortdrive',
            name='ShortDriveEligibility',
            field=models.CharField(max_length=5, null=True),
        ),
    ]
