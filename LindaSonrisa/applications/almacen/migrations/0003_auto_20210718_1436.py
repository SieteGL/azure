# Generated by Django 3.1.7 on 2021-07-18 18:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('almacen', '0002_almacen_proveedor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='disponible',
            name='precio_unitario',
        ),
        migrations.RemoveField(
            model_name='disponible',
            name='total',
        ),
    ]
