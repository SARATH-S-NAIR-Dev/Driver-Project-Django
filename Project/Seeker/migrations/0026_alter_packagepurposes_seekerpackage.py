# Generated by Django 3.2.10 on 2021-12-21 15:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Seeker', '0025_alter_seekerprofileshortdrive_shortdriveeligibility'),
    ]

    operations = [
        migrations.AlterField(
            model_name='packagepurposes',
            name='SeekerPackage',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Seeker.seekerprofilepackage'),
        ),
    ]
