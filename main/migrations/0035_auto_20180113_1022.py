# Generated by Django 2.0 on 2018-01-13 04:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0034_facility_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='facility',
        ),
        migrations.DeleteModel(
            name='Facility',
        ),
    ]