# Generated by Django 5.0.4 on 2024-04-29 20:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('touragency', '0008_tour_trips'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='promocode',
        ),
    ]