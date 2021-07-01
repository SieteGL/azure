# Generated by Django 3.1.7 on 2021-06-27 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_auto_20210624_1154'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='contacto',
            field=models.PositiveIntegerField(blank=True, default=1, verbose_name='Numero de contacto'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='numero',
            field=models.CharField(blank=True, max_length=6, verbose_name='Número de casa'),
        ),
    ]