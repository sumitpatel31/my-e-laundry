# Generated by Django 5.0.2 on 2024-03-10 01:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('e_laundry', '0002_alter_orders_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 3, 10, 6, 58, 16, 3155)),
        ),
    ]
