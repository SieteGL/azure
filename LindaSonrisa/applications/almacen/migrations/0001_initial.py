# Generated by Django 3.1.7 on 2021-07-14 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Almacen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(blank=True, max_length=17, verbose_name='codigo del producto')),
                ('nombre_producto', models.CharField(blank=True, max_length=25, verbose_name='Nombre del producto')),
                ('familia', models.CharField(blank=True, max_length=50, verbose_name='Familia')),
                ('descripcion', models.CharField(blank=True, max_length=50, verbose_name='Descripcion del producto')),
                ('fecha_vencimiento', models.DateField(blank=True, null=True, verbose_name='Fecha vencimiento')),
                ('cantidad', models.PositiveIntegerField(blank=True, verbose_name='Cantidad por producto')),
                ('precio_unitario', models.PositiveIntegerField(verbose_name='Precio unitario del producto')),
                ('total', models.PositiveIntegerField(blank=True, default=True, null=True, verbose_name='Total del producto')),
            ],
            options={
                'verbose_name': 'almacen',
                'verbose_name_plural': ' almacenaje',
            },
        ),
        migrations.CreateModel(
            name='Disponible',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(blank=True, max_length=17, verbose_name='codigo del producto')),
                ('nombre_producto', models.CharField(blank=True, max_length=25, verbose_name='Nombre del producto')),
                ('familia', models.CharField(blank=True, max_length=50, verbose_name='Familia')),
                ('fecha_vencimiento', models.DateField(blank=True, null=True, verbose_name='Fecha vencimiento')),
                ('stock', models.PositiveIntegerField(blank=True, verbose_name='Cantidad por producto')),
                ('stock_critico', models.PositiveIntegerField(blank=True, verbose_name='Stock critico')),
                ('precio_unitario', models.PositiveIntegerField(verbose_name='Precio unitario del producto')),
                ('total', models.PositiveIntegerField(blank=True, default=True, null=True, verbose_name='Total del producto')),
            ],
            options={
                'verbose_name': 'Disponible',
                'verbose_name_plural': 'Disponibles',
            },
        ),
        migrations.CreateModel(
            name='Familia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoria', models.CharField(blank=True, max_length=20, verbose_name='sub-tipo')),
            ],
            options={
                'verbose_name': 'sub-producto',
                'verbose_name_plural': 'familia de productos',
            },
        ),
    ]
