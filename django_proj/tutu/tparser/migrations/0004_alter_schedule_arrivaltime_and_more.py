# Generated by Django 4.0.6 on 2022-07-18 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tparser', '0003_alter_schedule_troikacardprice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='arrivalTime',
            field=models.TextField(verbose_name='Дата прибытия'),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='departureTime',
            field=models.TextField(verbose_name='Дата отправления'),
        ),
    ]