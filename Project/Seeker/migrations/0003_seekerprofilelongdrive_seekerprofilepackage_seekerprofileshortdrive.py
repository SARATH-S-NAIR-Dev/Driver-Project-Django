# Generated by Django 3.2.8 on 2021-11-19 17:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Guest', '0001_initial'),
        ('BasicEntry', '0008_rename_drivehours_drivehour'),
        ('Seeker', '0002_alter_seekertest_seekerid'),
    ]

    operations = [
        migrations.CreateModel(
            name='SeekerProfileShortDrive',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ShortDriveEligibility', models.CharField(max_length=5)),
                ('ShortDriveAmount', models.CharField(max_length=10)),
                ('SeekerID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Guest.newseeker')),
                ('ShortDriveDrivingHours', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BasicEntry.drivehour')),
                ('ShortDriveDrivingMode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BasicEntry.drivemode')),
                ('ShortDrivePurpose', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BasicEntry.shorttravelingpurpose')),
                ('ShortDriveVehicleModel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BasicEntry.vehiclemodel')),
                ('ShortDriveVehicleType', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BasicEntry.vehicletype')),
                ('ShortDriveWorkingDays', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BasicEntry.weekday')),
            ],
        ),
        migrations.CreateModel(
            name='SeekerProfilePackage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PackageEligibility', models.CharField(max_length=5)),
                ('PackageAmount', models.CharField(max_length=10)),
                ('PackageDrivingHours', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BasicEntry.drivehour')),
                ('PackageDrivingMode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BasicEntry.drivemode')),
                ('PackagePurpose', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BasicEntry.shorttravelingpurpose')),
                ('PackageVehicleModel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BasicEntry.vehiclemodel')),
                ('PackageVehicleType', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BasicEntry.vehicletype')),
                ('PackageWorkingDays', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BasicEntry.weekday')),
                ('SeekerID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Guest.newseeker')),
            ],
        ),
        migrations.CreateModel(
            name='SeekerProfileLongDrive',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('LongDriveEligibility', models.CharField(max_length=5)),
                ('LongDriveAmount', models.CharField(max_length=10)),
                ('LongDriveDrivingHours', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BasicEntry.drivehour')),
                ('LongDriveDrivingMode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BasicEntry.drivemode')),
                ('LongDrivePurpose', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BasicEntry.shorttravelingpurpose')),
                ('LongDriveVehicleModel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BasicEntry.vehiclemodel')),
                ('LongDriveVehicleType', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BasicEntry.vehicletype')),
                ('LongDriveWorkingDays', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BasicEntry.weekday')),
                ('SeekerID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Guest.newseeker')),
            ],
        ),
    ]
