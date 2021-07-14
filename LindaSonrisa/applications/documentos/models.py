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
            

class EspecialistaProcedimiento(models.Model):

    fecha = models.DateField(

    )
    especialista = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name='Especialista'
    )


#generar quien genera los procedimientos 
class Procedimientos(models.Model):
    """relacion con ficha tecnica"""

    #ODONTOLOGO GENERAL
    ODONTOLOGO = '0'
    #FRENILLOS | ORTODONCIA
    ORTODONCISTA = '1'
    #RADIOGRAFIAS | BITE WING 
    RADIOLOGO = '2'
    #PROTESIS
    PROSTODONCISTA = '3'

    PROCEDERES = [
        (ODONTOLOGO,'Odontologo General'),
        (ORTODONCISTA,'Ortodoncista'),
        (RADIOLOGO,'Radiologo'),
        (PROSTODONCISTA,'Prostodoncista'),
    ]      

    tipo_procedimiento = models.CharField(
        max_length=1,
        choices=PROCEDERES,
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
    Especialista_Procedimiento = models.ForeignKey(
        EspecialistaProcedimiento,
        on_delete=models.CASCADE,
        verbose_name='Procedimientos'
    )

    #agregar especialista a cargo ver como poner 2 valores de tipo User.models

    objects = ConsultasManager()

    class Meta:
        verbose_name_plural = 'Procedimientos'

    def __str__(self):
        return str(self.id)+' - '+str(self.cliente)
        

#view economico
class Documento(models.Model):

    LIQUIDACION = '0'
    FINIQUITO = '1'
    AFP  = '2'

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
    
    valor = models.IntegerField(
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
                

          