# Generated by Django 5.0.2 on 2024-03-01 02:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('e_laundry', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 3, 1, 7, 48, 15, 324953)),
        ),
    ]
