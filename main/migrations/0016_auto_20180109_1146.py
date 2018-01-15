# Generated by Django 2.0 on 2018-01-09 06:01

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_auto_20180109_1145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='expected_arrival_date_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 9, 11, 46, 43, 861312)),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='expected_departure_date_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 9, 11, 46, 43, 861331)),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='reservation_date_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 9, 11, 46, 43, 861281)),
        ),
        migrations.AlterField(
            model_name='room',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='room_customer', to='main.Reservation'),
        ),
    ]