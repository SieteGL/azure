from django.db import models
from django.conf import settings
from rest_framework.fields import ReadOnlyField

from applications.almacen.models import Almacen
#
from .managers import ServiciosManager

class ServiciosList(models.Model):
    
    servicio = models.CharField(
        'servicio prestado',
        max_length=120,
        unique=True,
        #editable=False
    ) 

    class Meta:
        verbose_name = 'Servicio'
        verbose_name_plural = 'Servicios prestados'

    def __str__(self):
        return str(self.id) +' - '+ self.servicio    


class Servicios(models.Model):
    

    servicios_lista = models.ManyToManyField(ServiciosList)             
            
    name = models.CharField(
        'paquete de servicio',
        max_length=25,
        blank=True
    )

    valor_paquete = models.IntegerField(
        'Valor paquete',
        blank=True
    )

    objects = ServiciosManager()   

    def __str__(self):
        return str(self.id)+' - '+str(self.name)+' - '+str(self.valor_paquete)
