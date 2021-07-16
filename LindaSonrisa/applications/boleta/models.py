from django.db import models
#
from applications.servicios.models import Servicios, ServiciosList
#
from applications.documentos.models import Documento
#
from applications.configuracion.models import Empresa
#from applications.documentos.models import Procedimientos
from applications.almacen.models import Almacen
#
from applications.users.models import User

#
from .managers import BoletaManager

class Boleta(models.Model):    

    boleta_numero = models.IntegerField(
        'Boleta N°...'
    )

    fecha_atencion = models.DateTimeField(
        'Fecha de atencion',
        blank=True,
        null=False
    )    
    empresa = models.ForeignKey(
        Empresa,
        on_delete=models.CASCADE
    )
    cliente = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    documento = models.CharField(     
        max_length=10,
        blank=True  
    )
    #Guardar el descuento realizado... NO ESTA EN EL CUADERNO
    descuento = models.IntegerField(
        'Descuento a realizar'
    )

    objects = BoletaManager()

#agregar empresa FK
    def __str__(self):
        return  str(self.id)+' - '+str(self.cliente)
            


class BoletaServicio(models.Model):

    boleta = models.ForeignKey(
        Boleta,
        on_delete=models.CASCADE,
        verbose_name='Boleta Cabecera'
    )
    
    serviciosList = models.ManyToManyField(Servicios)

    especialista = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    sub_total = models.IntegerField(
        'Sub-Total de la atencion',
        null=True
    )
    total = models.IntegerField(
        'Total operaciones',
        null=True
    )
    objects = BoletaManager()

#agregar fk de moneda
    class Meta:
        verbose_name = 'Detalle'
        verbose_name_plural = 'Detalles'

    def __str__(self):
        return  str(self.id)+'*********'+str(self.boleta)     
    