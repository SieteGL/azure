# Generated by Django 3.1.7 on 2021-07-18 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('configuracion', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='empresa',
            name='numeracion',
            field=models.IntegerField(default=1, verbose_name='Numeracion del establecimiento'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='empresa',
            name='codigo_area',
            field=models.CharField(blank=True, choices=[('0', '+54'), ('1', '+591'), ('2', '+595'), ('3', '+56'), ('4', '+57'), ('5', '+51'), ('6', '+598'), ('7', '+593'), ('8', '+52'), ('9', '+58')], max_length=4, verbose_name='Codigo area país'),
        ),
    ]
