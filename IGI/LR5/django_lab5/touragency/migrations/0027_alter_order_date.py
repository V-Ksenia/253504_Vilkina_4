# Generated by Django 5.0.4 on 2024-05-01 22:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('touragency', '0026_alter_order_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateField(default=datetime.datetime(2024, 5, 2, 1, 13, 34, 15395)),
        ),
    ]