# Generated by Django 4.0.6 on 2022-07-18 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tparser', '0004_alter_schedule_arrivaltime_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='arrivalTime',
            field=models.TextField(verbose_name='Время прибытия'),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='departureTime',
            field=models.TextField(verbose_name='Время отправления'),
        ),
    ]
