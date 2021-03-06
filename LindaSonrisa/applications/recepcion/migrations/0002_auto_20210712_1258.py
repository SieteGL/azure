# Generated by Django 3.1.7 on 2021-07-12 16:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('recepcion', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recepcion',
            name='receptor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Receptor de los productos'),
        ),
        migrations.AddField(
            model_name='orden',
            name='recepcion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Solicitante'),
        ),
        migrations.AddField(
            model_name='estado',
            name='orden',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='recepcion.orden', verbose_name='identificador tipo de orden'),
        ),
        migrations.AddField(
            model_name='estado',
            name='proveedores',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='proveedor da reporte'),
        ),
        migrations.AddField(
            model_name='detalles',
            name='ordenes',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recepcion.orden'),
        ),
        migrations.AddField(
            model_name='detalles',
            name='proveedor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Proveedor'),
        ),
    ]
