# Generated by Django 3.0 on 2020-12-04 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0013_auto_20200819_2318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='date_of_keeping',
            field=models.DateTimeField(auto_now=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='date_published',
            field=models.DateTimeField(auto_now=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='bookorder',
            name='order_date',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='date_of_membership',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]