# Generated by Django 3.1.7 on 2021-06-24 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_auto_20210624_1143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_cli',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_emp',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_esp',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_pro',
            field=models.BooleanField(default=False),
        ),
    ]
