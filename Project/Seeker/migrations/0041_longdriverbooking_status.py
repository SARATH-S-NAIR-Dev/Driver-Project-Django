# Generated by Django 3.2.10 on 2022-02-09 02:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Seeker', '0040_auto_20220209_0732'),
    ]

    operations = [
        migrations.AddField(
            model_name='longdriverbooking',
            name='Status',
            field=models.IntegerField(default=0),
        ),
    ]