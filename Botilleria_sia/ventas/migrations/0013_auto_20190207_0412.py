# Generated by Django 2.1.4 on 2019-02-07 04:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0012_auto_20190126_2310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venta',
            name='FECHA',
            field=models.DateField(blank=True, default=datetime.date(2019, 2, 7)),
        ),
        migrations.AlterField(
            model_name='venta',
            name='HORA',
            field=models.TimeField(blank=True, default=datetime.time(4, 12, 10, 328282)),
        ),
    ]
