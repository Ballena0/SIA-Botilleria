# Generated by Django 2.1.4 on 2019-01-06 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0005_venta_vendedor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detalle',
            name='CANTIDAD',
            field=models.IntegerField(default=1),
        ),
    ]