# Generated by Django 3.1.7 on 2021-06-15 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('configuracion', '0002_auto_20210614_0025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empresa',
            name='codigo_area',
            field=models.CharField(blank=True, choices=[('0', '+54'), ('1', '+591'), ('2', '+595'), ('3', '+56'), ('4', ''), ('5', ''), ('6', ''), ('7', ''), ('8', ''), ('9', '')], max_length=2, verbose_name='Codigo area país'),
        ),
    ]
