# Generated by Django 3.1.7 on 2021-06-24 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20210616_0210'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='cli',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='emp',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='esp',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='pro',
            field=models.BooleanField(default=False),
        ),
    ]