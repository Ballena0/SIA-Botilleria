# Generated by Django 2.1.3 on 2018-12-24 17:17

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('inventario', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DETALLE',
            fields=[
                ('DETALLE_ID', models.IntegerField(primary_key=True, serialize=False)),
                ('CANTIDAD', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='TIPO_PAGO',
            fields=[
                ('PAGO_ID', models.IntegerField(primary_key=True, serialize=False)),
                ('TIPO_PAGO', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='VENTA',
            fields=[
                ('VENTA_ID', models.IntegerField(primary_key=True, serialize=False)),
                ('FECHA', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('TOTAL_A_PAGAR', models.IntegerField(default=0)),
                ('TIPO_PAGO', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ventas.TIPO_PAGO')),
            ],
        ),
        migrations.AddField(
            model_name='detalle',
            name='NUMERO_DE_VENTA',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ventas.VENTA'),
        ),
        migrations.AddField(
            model_name='detalle',
            name='PRODUCTO',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.PRODUCTO'),
        ),
    ]
