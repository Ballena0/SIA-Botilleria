# Generated by Django 2.1.4 on 2019-01-07 17:16

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0005_registrobodega_cantidad'),
    ]

    operations = [
        migrations.CreateModel(
            name='IngresoProducto',
            fields=[
                ('IP_ID', models.AutoField(primary_key=True, serialize=False)),
                ('CANTIDAD', models.IntegerField(default=1)),
                ('DESCRIPCION', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('PEDIDO_ID', models.AutoField(primary_key=True, serialize=False)),
                ('FECHA', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('INGRESADO_POR', models.CharField(max_length=50)),
                ('PROVEEDOR', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.PROVEEDOR')),
            ],
        ),
        migrations.RemoveField(
            model_name='registrobodega',
            name='PRODUCTO',
        ),
        migrations.RemoveField(
            model_name='registrobodega',
            name='PROVEEDOR',
        ),
        migrations.DeleteModel(
            name='RegistroBodega',
        ),
        migrations.AddField(
            model_name='ingresoproducto',
            name='PEDIDO',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.Pedido'),
        ),
        migrations.AddField(
            model_name='ingresoproducto',
            name='PRODUCTO',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.PRODUCTO'),
        ),
    ]
