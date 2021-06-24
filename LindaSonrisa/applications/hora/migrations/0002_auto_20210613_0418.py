# Generated by Django 3.1.7 on 2021-06-13 08:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hora', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='agenda',
            name='especialista_agenda',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='users.user', verbose_name='Agenda del espacialista'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reserva',
            name='hora_cliente',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='users.user', verbose_name='hora del cliente'),
            preserve_default=False,
        ),
    ]
