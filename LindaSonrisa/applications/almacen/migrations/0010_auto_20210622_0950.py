# Generated by Django 3.1.7 on 2021-06-22 13:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('almacen', '0009_auto_20210622_0948'),
    ]

    operations = [
        migrations.RenameField(
            model_name='almacen',
            old_name='cantidad',
            new_name='stock',
        ),
    ]
