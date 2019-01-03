# Generated by Django 2.1.4 on 2018-12-29 00:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0003_proveedor'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegistroBodega',
            fields=[
                ('REGBOD_ID', models.AutoField(primary_key=True, serialize=False)),
                ('DESCRIPCION', models.CharField(max_length=100)),
                ('PRODUCTO', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.PRODUCTO')),
                ('PROVEEDOR', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.PROVEEDOR')),
            ],
        ),
    ]