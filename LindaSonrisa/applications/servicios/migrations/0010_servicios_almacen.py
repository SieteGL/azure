# Generated by Django 3.1.7 on 2021-06-17 16:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('almacen', '0007_almacen_num_sale'),
        ('servicios', '0009_auto_20210615_2344'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicios',
            name='almacen',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='almacen_servicio', to='almacen.almacen', verbose_name='producto para servicio'),
            preserve_default=False,
        ),
    ]
