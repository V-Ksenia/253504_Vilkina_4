# Generated by Django 5.0.4 on 2024-05-01 22:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('touragency', '0023_order_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 2, 1, 6, 8, 711487)),
        ),
    ]