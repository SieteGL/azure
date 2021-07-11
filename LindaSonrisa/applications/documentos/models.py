from django.db import models
from django.db.models.enums import Choices
from django.conf import settings
#
from applications.users.models import User
#
from .managers import ConsultasManager

class FichaTecnica(models.Model):
    
    ENFERMEDAD = (
        ('S','SI'),
        ('N','NO'),        
    )

    ALERGIA = (
        ('S','SI'),
        ('N','NO'),  
    )

    enfermedad = models.CharField(
        max_length=1,
        choices=ENFERMEDAD,
        blank=True
    )

    alergia = models.CharField(
        max_length=1,
        choices=ALERGIA,
        blank=True
    )    

    enfermedades = models.TextField(
        max_length=250,
        blank=True
    )

    alergias = models.TextField(
        max_length=250,
        blank=True
    )

    cliente = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE, 
        verbose_name='Cliente'
    )

    objects = ConsultasManager()

    class Meta:
        verbose_name = 'Ficha tecnica'

    def __str__(self):
        return str(self.id)
            

#generar quien genera los procedimientos 
class Procedimientos(models.Model):
    """relacion con ficha tecnica"""

    PROCEDIMIENTO = (
        ('0','FRENILLOS'),
        ('1','REVISON'),
        ('2','TAPADURA'),
        ('3','EXTRACCION'),
        ('4','CORONA'),
        ('5','TRATAMIENTO CONDUCTO'),
    )
    
    fecha_procedimientos = models.DateField(
        'Fecha del procedimiento',
        blank=True,
        null=True
    )

    tipo_procedimiento = models.CharField(
        max_length=1,
        choices=PROCEDIMIENTO,
        blank=True
    )

    descripcion_procedimiento = models.TextField(
        'Descripcion de o los procedimientos',
        max_length=250,
        blank=True
    )

    cliente = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name='Cliente'
    )

    #agregar especialista a cargo ver como poner 2 valores de tipo User.models

    objects = ConsultasManager()

    class Meta:
        verbose_name_plural = 'Procedimientos'

    def __str__(self):
        return str(self.id)+' - '+str(self.fecha_procedimientos)
        

#view economico
class Documento(models.Model):

    ARCHIVO = (
        ('0','LIQUIDACION'),
        ('1','FINIQUITO'),
        ('2','AFP'),    
    )

    documento = models.CharField(
        max_length=100,
        choices=ARCHIVO,
        blank=True
    )
    
    valor = models.CharField(
        max_length=250,
        blank=True
    )

    imagen = models.ImageField(
        'Imagen',
        blank=True, 
        null=True,
        upload_to='Documento',
    )

    cliente = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    objects = ConsultasManager()

    class Meta:
        verbose_name = 'Documento cargado'
        verbose_name_plural = 'Documentos cargados'

    def __str__(self):
        return str(self.id)+' - '+ str(self.documento)
                

          