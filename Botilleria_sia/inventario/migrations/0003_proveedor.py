# Generated by Django 2.1.3 on 2018-12-26 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0002_auto_20181224_2032'),
    ]

    operations = [
        migrations.CreateModel(
            name='PROVEEDOR',
            fields=[
                ('RUT', models.IntegerField(primary_key=True, serialize=False)),
                ('NOMBRE', models.CharField(max_length=50)),
                ('TELEFONO', models.IntegerField(default=0)),
            ],
        ),
    ]
