# Generated by Django 3.1.7 on 2021-07-14 05:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Detalles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(blank=True, max_length=17, verbose_name='codigo del producto')),
                ('nombre_producto', models.CharField(blank=True, max_length=25, verbose_name='Nombre del producto')),
                ('familia', models.CharField(blank=True, max_length=50, verbose_name='tipo producto')),
                ('descripcion', models.CharField(blank=True, max_length=50, verbose_name='Descripcion del producto')),
                ('fecha_vencimiento', models.DateField(blank=True, max_length=10, null=True, verbose_name='Fecha vencimiento')),
                ('cantidad', models.PositiveIntegerField(blank=True, verbose_name='Cantidad por producto')),
                ('precio_unitario', models.PositiveIntegerField(verbose_name='Precio unitario del producto')),
                ('total', models.PositiveIntegerField(blank=True, default=True, null=True, verbose_name='Total del producto')),
                ('valid', models.BooleanField(default=False, null=True)),
                ('recepcionado', models.BooleanField()),
            ],
            options={
                'verbose_name': '2- Detalles de las compra',
            },
        ),
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estados', models.CharField(blank=True, choices=[('0', 'Procesando'), ('1', 'Preparando'), ('2', 'Despachado'), ('3', 'Encamino'), ('4', 'Entregado'), ('5', 'Finalizado')], max_length=1)),
                ('observacion', models.TextField(max_length=100, verbose_name='Observaciones')),
            ],
            options={
                'verbose_name': '4- Estados del producto',
                'verbose_name_plural': '4- Estados de los productos',
            },
        ),
        migrations.CreateModel(
            name='Orden',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(verbose_name='Fecha compra')),
                ('name', models.CharField(blank=True, max_length=25, verbose_name='Nombre de la orden')),
            ],
            options={
                'verbose_name': '1- Orden N°',
            },
        ),
        migrations.CreateModel(
            name='Recepcion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valido', models.BooleanField()),
                ('agregado', models.BooleanField(default=False)),
                ('detalles_recepcion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recepcion.detalles', verbose_name='Detalles del pedido recepcionado')),
            ],
            options={
                'verbose_name': '3- Recepcion de productos',
                'verbose_name_plural': '4- Recepcion de los productos',
            },
        ),
    ]
