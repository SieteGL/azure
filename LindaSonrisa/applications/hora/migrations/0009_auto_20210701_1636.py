# Generated by Django 3.1.7 on 2021-07-01 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hora', '0008_auto_20210620_0611'),
    ]

    operations = [
        migrations.AddField(
            model_name='reserva',
            name='fecha',
            field=models.DateField(null=True, verbose_name='Fecha de hora tomada'),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='hora',
            field=models.CharField(max_length=6, null=True, verbose_name='Hora tomada'),
        ),
    ]
