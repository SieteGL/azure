from django.db import models
from django.conf import settings
#
from applications.almacen.models import Almacen
from applications.users.models import User
#
from .managers import RecepcionManager


#comprando
class Orden(models.Model):
    #quien creo la orden para tener un identificador del usuario que la creo 
    fecha = models.DateField(
        'Fecha compra'
    )       
    name = models.CharField(
        'Nombre de la orden',
        max_length=25,
        blank=True
    )
    recepcion = models.ForeignKey(        
        User,
        on_delete=models.CASCADE,
        verbose_name='Solicitante'
    )

    objects = RecepcionManager()

    class Meta:
        verbose_name = '1- Orden N°'

    def __str__(self):
        return str(self.id)+' - '+str(self.fecha)+' - '+str(self.name)

#comprando
class Detalles(models.Model):

    ordenes = models.ForeignKey(
        Orden,
        on_delete=models.CASCADE
    )

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
    proveedor = models.EmailField(
        'Email proveedor',
        blank=True,
        null=True
    )
    almacen = models.ForeignKey(
        Almacen,
        on_delete=models.CASCADE,
        verbose_name='ALMACEN ACTUALIZAR PRODUCTOS',
        null=True
    )
    valid = models.BooleanField(default=False,null=True)

    objects = RecepcionManager()

    class Meta:
        verbose_name = '2- Detalles de las compra'

    def __str__(self):
        return str(self.id)+' - '+str(self.nombre_producto) 
        

class Estado(models.Model):
    
    PROCESANDO = '0'
    PREPARANDO = '1'
    DESPACHADO = '2'
    ENCAMINO = '3'
    ENTREGADO = '4'
    FINALIZADO = '5'

    ESTADO_CHOICES = [
        (PROCESANDO,'Procesando'),
        (PREPARANDO,'Preparando'),
        (DESPACHADO,'Despachado'),
        (ENCAMINO,'Encamino'),
        (ENTREGADO,'Entregado'),
        (FINALIZADO,'Finalizado'),
    ]

    orden = models.OneToOneField(
        Orden,
        on_delete=models.CASCADE,
        verbose_name='identificador tipo de orden',
        #unique = true fue agregado para que no se pudiera ingresar mas de un reporte por nombnre de orden
        #unique=True
    )
 
    proveedores = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='proveedor da reporte'
    )

    estados = models.CharField(        
        choices=ESTADO_CHOICES,
        max_length=1,
        blank=True
    )

    observacion = models.TextField(
        'Observaciones',
        max_length=100
    )

    
    objects = RecepcionManager()

    class Meta:
        verbose_name = "4- Estados del producto"
        verbose_name_plural = '4- Estados de los productos'
 
    def __str__(self):
        return str(self.id)+str(self.orden)


class Recepcion(models.Model):

    receptor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="Receptor de los productos",        
    )
    
    #revisar id de recepcion o algun identificador.
    detalles_recepcion = models.ForeignKey(
        Detalles,
        on_delete=models.CASCADE,
        verbose_name='Detalles del pedido recepcionado'
    )

    almacen = models.ForeignKey(
        Almacen,
        on_delete=models.CASCADE,
        verbose_name='ALMACEN ACTUALIZAR PRODUCTOS'
    )
    #lo recibido concuerda con lo pedido
    valido = models.BooleanField()

    class Meta:
        verbose_name='3- Recepcion de productos'
        verbose_name_plural = '4- Recepcion de los productos'
    def __str__(self):
        return str(self.id)+' - '+str(self.detalles_recepcion)+ ' - '+str(self.receptor)



