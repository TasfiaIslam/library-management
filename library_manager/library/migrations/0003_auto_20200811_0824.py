# Generated by Django 3.0.8 on 2020-08-11 02:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_auto_20200811_0813'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookorder',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Out for delivery', 'Out for delivery'), ('Delivered', 'Delivered')], max_length=200, null=True),
        ),
    ]
