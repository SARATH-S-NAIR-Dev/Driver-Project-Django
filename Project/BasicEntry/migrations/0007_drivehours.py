# Generated by Django 3.2.8 on 2021-11-19 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BasicEntry', '0006_auto_20211119_2218'),
    ]

    operations = [
        migrations.CreateModel(
            name='DriveHours',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Time', models.CharField(max_length=10)),
            ],
        ),
    ]
