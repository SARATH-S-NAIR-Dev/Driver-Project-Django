# Generated by Django 3.2.10 on 2022-02-08 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Seeker', '0038_shortdriverbooking_moreinfo'),
    ]

    operations = [
        migrations.AddField(
            model_name='shortdriverbooking',
            name='actualtotalamount',
            field=models.CharField(default='00.00', max_length=20),
        ),
        migrations.AddField(
            model_name='shortdriverbooking',
            name='workcompletionremarks',
            field=models.CharField(default='No Remarks', max_length=20),
        ),
    ]
