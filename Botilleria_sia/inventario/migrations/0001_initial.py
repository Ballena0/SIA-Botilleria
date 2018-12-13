# Generated by Django 2.1.4 on 2018-12-09 03:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FORMATO',
            fields=[
                ('FORMATO_ID', models.IntegerField(primary_key=True, serialize=False)),
                ('CANTIDAD', models.IntegerField(default=0)),
                ('CANT_P', models.IntegerField(default=0)),
                ('TIPO_FORMATO', models.CharField(max_length=50)),
                ('DESCRIPCION_FOR', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='PRODUCTO',
            fields=[
                ('ID_PROD', models.IntegerField(primary_key=True, serialize=False)),
                ('NOMBRE_PROD', models.CharField(max_length=50)),
                ('PRECIO', models.IntegerField(default=0)),
                ('STOCK', models.IntegerField(default=0)),
                ('DESCRIPCION_PROD', models.CharField(max_length=50)),
                ('FORM_PROD', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.FORMATO')),
            ],
        ),
    ]
