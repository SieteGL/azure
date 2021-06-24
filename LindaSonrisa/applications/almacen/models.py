from django.db import models
from django.conf import settings
#
#from applications.users.models import User
#
from .managers import AlmacenManager

class Familia(models.Model):
        

    categoria = models.CharField(        
        'sub-tipo',
        max_length=20,
        blank=True
    )

    class Meta:
        verbose_name = 'sub-producto'
        verbose_name_plural = 'familia de productos'

    def __str__(self):
        return str(self.familia)+' - '+(self.categoria)
    
class Almacen(models.Model):

    codigo = models.CharField(
        'codigo del producto',
        max_length=17,
        blank=True
    )

    nombre_producto = models.CharField(
        'Nombre del producto',
        max_length=25,
        blank=True
    )

    familia = models.CharField(
        'tipo producto',
        max_length=50,
        blank=True
    )

    descripcion = models.CharField(
        'Descripcion del producto',
        max_length=50,
        blank=True
    ) 

    fecha_vencimiento = models.DateField(
        'Fecha vencimiento',
        blank=True,
        null=True,

    )   

    cantidad = models.PositiveIntegerField(
        'Cantidad por producto',
        blank=True
    )

    precio_unitario = models.PositiveIntegerField(
        'Precio unitario del producto',        
    )

    total = models.PositiveIntegerField(
        'Total del producto',
        null=True,
        default=True,
        blank=True,        
    )
    #
    
    empleado = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    objects = AlmacenManager()
    
    class Meta:
        verbose_name= 'almacen'
        verbose_name_plural = ' almacenaje'

    def __str__(self):
        return str(self.nombre_producto)+' - '+str(self.codigo)
        
            
    