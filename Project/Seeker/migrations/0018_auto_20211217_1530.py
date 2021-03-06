# Generated by Django 3.2.10 on 2021-12-17 10:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('BasicEntry', '0008_rename_drivehours_drivehour'),
        ('Seeker', '0017_auto_20211217_1508'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='seekerprofilepackage',
            name='PackagePurpose',
        ),
        migrations.CreateModel(
            name='PackagePurposes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Purposes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BasicEntry.packagetravelingpurpose')),
                ('SeekerPackage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Seeker.seekerprofilelongdrive')),
            ],
        ),
    ]
