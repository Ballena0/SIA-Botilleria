# Generated by Django 2.1.4 on 2019-02-07 04:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0013_auto_20190207_0412'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venta',
            name='HORA',
            field=models.TimeField(blank=True, default=datetime.time(4, 20, 32, 987429)),
        ),
    ]
