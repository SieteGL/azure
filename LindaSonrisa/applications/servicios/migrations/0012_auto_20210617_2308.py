# Generated by Django 3.1.7 on 2021-06-18 03:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('servicios', '0011_remove_servicios_almacen'),
    ]

    operations = [
        migrations.RenameField(
            model_name='servicios',
            old_name='serviciosList',
            new_name='servicios_listar',
        ),
    ]
