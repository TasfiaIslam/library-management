# Generated by Django 3.0 on 2020-12-04 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0015_auto_20201204_2004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='date_of_keeping',
            field=models.DateTimeField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='date_published',
            field=models.DateTimeField(max_length=200, null=True),
        ),
    ]
