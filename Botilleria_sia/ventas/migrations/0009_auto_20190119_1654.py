# Generated by Django 2.1.4 on 2019-01-19 16:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0008_detalle_estado'),
    ]

    operations = [
        migrations.AddField(
            model_name='venta',
            name='HORA',
            field=models.TimeField(blank=True, default=datetime.time(16, 54, 24, 757162)),
        ),
        migrations.AlterField(
            model_name='venta',
            name='FECHA',
            field=models.DateField(blank=True, default=datetime.date(2019, 1, 19)),
        ),
    ]
