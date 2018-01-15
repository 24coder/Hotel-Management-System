# Generated by Django 2.0 on 2018-01-13 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0035_auto_20180113_1022'),
    ]

    operations = [
        migrations.CreateModel(
            name='Facility',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
            ],
            options={
                'verbose_name_plural': 'Facilities',
            },
        ),
        migrations.AddField(
            model_name='room',
            name='facility',
            field=models.ManyToManyField(to='main.Facility'),
        ),
    ]