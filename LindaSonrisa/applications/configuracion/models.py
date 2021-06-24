from django.db import models

class Empresa(models.Model):

    COUNTRY = (
        ('0','ARGENTINA'),
        ('1','BOLIVIA'),
        ('2','PARAGUAY'),
        ('3','CHILE'),
        ('4','COLOMBIA'),
        ('5','PERÚ'),
        ('6','URUGUAY'),
        ('7','ECUADOR'),
        ('8','MÉXICO'),
        ('9','VENEZUELA'),
    )

    AREA = (
        ('0','+54'),
        ('1','+591'),
        ('2','+595'),
        ('3','+56'),
        ('4',''),
        ('5',''),
        ('6',''),
        ('7',''),
        ('8',''),
        ('9',''),
    )
    #agregar numeros faltantes al area

    nombre_empresa = models.CharField(
        'Nombre de la empresa',
        max_length=30,
        blank=True
    )

    rut = models.CharField(
        'Rut Empresa',
        max_length=12,
        blank = True 
    )

    pais = models.CharField(
        'País',
        max_length=2,
        choices=COUNTRY,
        blank=True
    )
    
    codigo_area = models.CharField(
        'Codigo area país',
        max_length=4,
        choices=AREA,
        blank=True
    )
    contacto = models.PositiveIntegerField(
        'Telefono de contacto'
    )

    año_fundacion = models.DateTimeField(
        'Fecha de fundacion',
        blank=True,
        #puede ser nulo 
        null=True
    )

    representante = models.CharField(
        'Nombre representante',
        max_length=30,
        blank=True
    )

    region = models.CharField(
        'Region',
        max_length=30,
        blank=True
    )

    comuna = models.CharField(
        'Comuna',
        max_length=30,
        blank=True
    )

    calle = models.CharField(
        'calle',
        max_length=30,
        blank=True
    )    

    def get_pias_display(self):                
        return ''.join([pais for pais in self.pais[:100]])


    get_pias_display.short_description = 'País'

    class Meta:
        verbose_name = 'Empresa detalles'
    
    def __str__(self):
        return str(self.id)+' - '+str(self.get_pias_display())


class Moneda(models.Model):

    MONEDA_CHOICES = (
        ('$','PESO'),
        ('Є','EURO'),
        ('$','DOLAR'),
    )

    moneda = models.CharField(
        max_length=1,
        choices=MONEDA_CHOICES,
        blank=True
    )    

    class Meta:
        verbose_name = 'Tipo de moneda'
        verbose_name_plural = 'Tipos de monedas'

    def __str__(self):
        return str(self.id)+' - '+ str(self.moneda)
        