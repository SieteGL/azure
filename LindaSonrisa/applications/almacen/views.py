from django.shortcuts import render
from rest_framework import serializers
#
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    ListCreateAPIView
)
from rest_framework.serializers import Serializer
#
from rest_framework.response import Response
#
from .serializers import (
    AlmacenSerializers,
    AlmaceSerializers,
    PruebaSerializers
    # AlmacenSerializers
)

from .models import Almacen, Disponible
from applications.recepcion.models import Detalles, Recepcion


class CargarAlmacen(CreateAPIView):
    serializer_class = AlmaceSerializers

    def create(self, request, *args, **kwargs):
        serializer = AlmaceSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        almacen = serializer.validated_data['almacen']
        list_almacen = []    
        list_disponibles = []

        for alcen in almacen:
            obj_almacen = Recepcion.objects.get(id=alcen['pk'])
            agregado = obj_almacen.agregado
            valido = obj_almacen.valido
            #--
            codig = obj_almacen.detalles_recepcion.codigo
            nombre = obj_almacen.detalles_recepcion.nombre_producto
            #--
            if agregado == False and valido == True:
                almacen_obj = Almacen(
                    codigo=obj_almacen.detalles_recepcion.codigo,
                    nombre_producto=obj_almacen.detalles_recepcion.nombre_producto,
                    familia=obj_almacen.detalles_recepcion.familia,
                    descripcion=obj_almacen.detalles_recepcion.descripcion,
                    fecha_vencimiento=obj_almacen.detalles_recepcion.fecha_vencimiento,
                    cantidad=obj_almacen.detalles_recepcion.cantidad,
                    precio_unitario=obj_almacen.detalles_recepcion.precio_unitario,
                    total=obj_almacen.detalles_recepcion.total,
                    proveedor=obj_almacen.detalles_recepcion.proveedor
                )
                list_almacen.append(almacen_obj)
                Almacen.objects.bulk_create(list_almacen)
                obj_almacen.agregado = True                
                obj_almacen.save()
                #---#
                disp = Disponible.objects.all()
                
                for eje in disp:
                    code = eje.codigo
                    prod_nombre = eje.nombre_producto
                    print('for')
                    print(code)
                    print(prod_nombre)
                    #----

                    #codigo y nombre iguales ya que codigo tiene la fecha de vencimiento
                if code != codig and prod_nombre != nombre: 
                    disponibles =Disponible(
                        codigo = almacen_obj.codigo,
                        nombre_producto = almacen_obj.nombre_producto,
                        familia = almacen_obj.familia,
                        fecha_vencimiento = almacen_obj.fecha_vencimiento,
                        stock = almacen_obj.cantidad,
                        stock_critico = 25
                    )
                    list_disponibles.append(disponibles)
                    Disponible.objects.bulk_create(list_disponibles)                
                elif code == codig and prod_nombre == nombre:
                    print('antes')
                    
                
                    eje.stock = eje.stock + obj_almacen.detalles_recepcion.cantidad
                    eje.save()
                    print('despues')
                    print(eje.stock)
                    

                return Response({'SUCCESS': 'AGREGADO AL ALMACEN'})
            elif agregado == True:
                return Response({'ERROR': 'PRODUCTO YA AGREGADO AL ALMACEN'})


class ListAlmacen(ListAPIView):
    serializer_class = AlmacenSerializers

    def get_queryset(self):
        return Almacen.objects.all()


"""
se crea una clase 'disponible' donde pondremos los productos con sus nombres para
hacer una lista de lo que esta disponible hacer una convergencia de todos los 
productos iguales ya sea por nombre, fecha_vencimiento,   
se dejara almacen para hacer la union de estos productos.
"""


# class CrearDisponibles(CreateAPIView):
#     serializer_class = AlmaceSerializers

#     def create(self, request, *args, **kwargs):
#         serializer = AlmaceSerializers(data=request.data)
#         serializer.is_valid(raise_exception=True)


"""
class ListarAlmacen(ListAPIView):
    serializer_class = AlmacenSerializers

    def get(self, request, *args, **kwargs):
        code = self.request.query_params.get('code'),
        fechaIn = self.request.query_params.get('dateI'),
        fechaFn = self.request.query_params.get('dateF'),
        stock = self.request.query_params.get('stock'),
        precio = self.request.query_params.get('precio'),
        #
        return Almacen.objects.filtrar_almacen(code)
                              

#realizar la carga del almacen en applications.ordenes        


#agregar producto al almacen y generar codigo. 

class CargarAlmacenRecepcion(CreateAPIView):
    serializer_class = ActualizarSerializer
    
    def create(self, request, *args, **kwargs):
        serializer = ActualizarSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
    
        receptor = serializer.validated_data['detalless']
        valid = serializer.validated_data['valido']
        lista_recepcion = []

        for dtl in receptor:
            almacenaje = Detalles.objects.get(id=dtl['pk']) 
            #variable almacenaje tiene los productos por id ver como listarlos por pantalla
        
            validaciones = valid
            if validaciones == True:
                alm = Almacen(
                    codigo = almacenaje.codigo,
                    nombre_producto = almacenaje.nombre_producto,
                    familia = almacenaje.familia,
                    descripcion = almacenaje.descripcion,
                    fecha_vencimiento = almacenaje.fecha_vencimiento,
                    cantidad = almacenaje.cantidad,
                    precio_unitario = almacenaje.precio_unitario,
                    total = almacenaje.total,
                    empleado = self.request.user
                )
                lista_recepcion.append(alm)
                return Response({'RES' : 'No valido'})
        Almacen.objects.bulk_create(lista_recepcion)              
        return Response({'res': 'ok'})





# funciona hasta aquí
                #----------------------------#
                #dispo = Disponible.objects.all()
                # if dispo.nombre_producto != obj_almacen.detalles_recepcion.nombre_producto:
                disponible = Disponible.objects.create(
                    # obj_almacen es un objeto de recepcion
                    codigo=obj_almacen.detalles_recepcion.codigo,
                    nombre_producto=obj_almacen.detalles_recepcion.nombre_producto,
                    familia=obj_almacen.detalles_recepcion.familia,
                    fecha_vencimiento=obj_almacen.detalles_recepcion.fecha_vencimiento,
                    stock=obj_almacen.detalles_recepcion.cantidad,
                    stock_critico=critico,
                    precio_unitario=obj_almacen.detalles_recepcion.precio_unitario,
                    total=obj_almacen.detalles_recepcion.total
                )
                #list_disponibles.append(disponible)
                if disponible.nombre_producto != obj_almacen.detalles_recepcion.nombre_producto:
                    disponible.save()

                print('stock actualizado')

                stock_actualizado = disponible.stock + \
                    obj_almacen.detalles_recepcion.cantidad
                

                # actualizar existencias
                if disponible.nombre_producto == obj_almacen.detalles_recepcion.nombre_producto:
                    disponible = Disponible(
                        # obj_almacen es un objeto de recepcion
                        codigo=obj_almacen.detalles_recepcion.codigo,
                        nombre_producto=obj_almacen.detalles_recepcion.nombre_producto,
                        familia=obj_almacen.detalles_recepcion.familia,
                        fecha_vencimiento=obj_almacen.detalles_recepcion.fecha_vencimiento,
                        stock=stock_actualizado,
                        precio_unitario=obj_almacen.detalles_recepcion.precio_unitario,
                        stock_critico=disponible.stock_critico
                    )
                    disponible.save()
                    return Response({'SUCCESS': 'ACTUALIZADO CON EXITO EN DISPONIBLES'})
                # elif dsp.nombre_producto != obj_almacen.detalles_recepcion.nombre_producto:

                #     return Response({'SUCCESS': 'AGREGADO A DISPONIBLES'})
                    #---#

"""


class ListAlmacenFiltro(ListAPIView):
    serializer_class = AlmacenSerializers

    def get_queryset(self):        
        stockI = self.request.query_params.get('stockI', None)
        stockF = self.request.query_params.get('stockF', None)
        if stockI is None:
            return Almacen.objects.all()
        else:
            return Almacen.objects.filtrar_almacen(
            stockI = stockI,
            stockF = stockF
            )