# Generated by Django 2.1.4 on 2018-12-28 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0003_auto_20181227_1836'),
    ]

    operations = [
        migrations.AddField(
            model_name='detalle',
            name='TOTAL_DETALLE',
            field=models.IntegerField(default=0),
        ),
    ]
