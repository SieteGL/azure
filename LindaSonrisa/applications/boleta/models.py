from django.db import models
#
from applications.servicios.models import Servicios, ServiciosList
from applications.configuracion.models import Empresa
#from applications.documentos.models import Procedimientos
from applications.almacen.models import Almacen
#
from applications.users.models import User

#
from .managers import BoletaManager

class Boleta(models.Model):    
        
    empresa = models.ForeignKey(
        Empresa,
        on_delete=models.CASCADE
    )
    cliente = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    serviciosList = models.ManyToManyField(ServiciosList)

#agregar empresa FK
    def __str__(self):
        return  str(self.id)+' - '+str(self.cliente)
            


class BoletaServicio(models.Model):
    #aca esta el problema
    """
    valor_unitario = models.IntegerField(
        "Valor por unidad"
    )
    """
    cantidad = models.IntegerField(
        "Cantidad de productos"
    )

    valor_total = models.IntegerField(
        "Valor total productos"
    )

    fecha_atencion = models.DateTimeField(
        'Fecha de atencion',
        blank=True,
        null=False
    )
    
    #serializar para detalles
    boleta = models.ForeignKey(
        Boleta, 
        on_delete=models.CASCADE,
        verbose_name='boleta'
    )

    almacen = models.ForeignKey(
        Almacen,
        on_delete=models.CASCADE,
        verbose_name='almacen'
    )

    #serializar para detalles
    """procedimiento = models.ForeignKey(
        Procedimientos,
        on_delete=models.CASCADE,
        verbose_name='Procedimiento paciente'
    )
    """
    objects = BoletaManager()

#agregar fk de moneda
    class Meta:
        verbose_name = 'Detalle'
        verbose_name_plural = 'Detalles'

    def __str__(self):
        return  str(self.fecha_atencion)     
    