# Generated by Django 3.2.10 on 2021-12-17 09:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('BasicEntry', '0008_rename_drivehours_drivehour'),
        ('Seeker', '0014_auto_20211217_1424'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seekerprofilepackage',
            name='PackagePurpose',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BasicEntry.packagetravelingpurpose'),
        ),
    ]
