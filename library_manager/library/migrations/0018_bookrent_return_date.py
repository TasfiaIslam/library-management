# Generated by Django 3.0 on 2020-12-14 01:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0017_auto_20201208_0207'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookrent',
            name='return_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
