# Generated by Django 3.0 on 2020-12-14 02:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0020_auto_20201214_0819'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookrent',
            name='rental_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='bookrent',
            name='return_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]