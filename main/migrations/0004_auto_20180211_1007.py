# Generated by Django 2.0 on 2018-02-11 04:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_staff_profilepic'),
    ]

    operations = [
        migrations.RenameField(
            model_name='staff',
            old_name='profilepic',
            new_name='profile_picture',
        ),
    ]