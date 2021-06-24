from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_empresa', models.CharField(blank=True, max_length=30, verbose_name='Nombre de la empresa')),
                ('rut', models.CharField(blank=True, max_length=12, verbose_name='Rut Empresa')),
                ('pais', models.CharField(blank=True, choices=[('0', 'ARGENTINA'), ('1', 'BOLIVIA'), ('2', 'PARAGUAY'), ('3', 'CHILE'), ('4', 'COLOMBIA'), ('5', 'PERÚ'), ('6', 'URUGUAY'), ('7', 'ECUADOR'), ('8', 'MÉXICO'), ('9', 'VENEZUELA')], max_length=2, verbose_name='País')),
                ('codigo_area', models.CharField(blank=True, choices=[('0', '+54'), ('1', '+591'), ('2', '+595'), ('3', '+56'), ('4', ''), ('5', ''), ('6', ''), ('7', ''), ('8', ''), ('9', '')], max_length=2, verbose_name='Codigo area país')),
                ('año_fundacion', models.DateTimeField(blank=True, null=True, verbose_name='Fecha de fundacion')),
                ('representante', models.CharField(blank=True, max_length=30, verbose_name='Nombre representante')),
                ('region', models.CharField(blank=True, max_length=30, verbose_name='Region')),
                ('comuna', models.CharField(blank=True, max_length=30, verbose_name='Comuna')),
                ('calle', models.CharField(blank=True, max_length=30, verbose_name='calle')),
            ],
            options={
                'verbose_name': 'Empresa detalles',
            },
        ),
        migrations.CreateModel(
            name='Moneda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('moneda', models.CharField(blank=True, choices=[('$', 'PESO'), ('Є', 'EURO'), ('$', 'DOLAR')], max_length=1)),
            ],
            options={
                'verbose_name': 'Tipo de moneda',
                'verbose_name_plural': 'Tipos de monedas',
            },
        ),
    ]
