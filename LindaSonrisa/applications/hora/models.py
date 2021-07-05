from django.db import models
from django.conf import settings
#
from applications.users.models import User
#
from .managers import AgendaManager
#especialista
class Agenda(models.Model):
    
    fecha = models.DateField(
        'Fecha disponibles',
        null=True     
    )

    hora = models.CharField(
        'hora ofrecida',
        max_length=6,
        null=True        
    )

    especialista_agenda = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name = 'Agenda del espacialista',
        null=True  
    )

    objects = AgendaManager()

    class Meta:
        verbose_name = 'agenda especialista'

    def __str__(self):
        return str(self.id)+' - '+str(self.fecha)
    

"""Hacer falta completo el modulo Revisar como importar un usuario en especifico."""

#cliente
class Reserva(models.Model):

    fecha = models.DateField(
        'Fecha de hora tomada',
        null=True     
    )

    hora = models.CharField(
        'Hora tomada',
        max_length=6,
        null=True        
    )

    hora_cliente = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name = 'hora del cliente'
    )

    objects = AgendaManager()

