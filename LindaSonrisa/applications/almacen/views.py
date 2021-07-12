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
    AlmaceSerializers    
    #AlmacenSerializers
    )

from .models import Almacen
from applications.recepcion.models import Detalles,Recepcion

class CargarAlmacen(CreateAPIView):
    serializer_class=AlmaceSerializers

    def create(self,request,*args,**kwargs):
        serializer = AlmaceSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)

        almacen = serializer.validated_data['almacen']
        list_almacen=[]

        for alcen in almacen:  
              
            obj_almacen=Recepcion.objects.get(id=alcen['pk'])
            agregado =obj_almacen.agregado
            valido = obj_almacen.valido

            if agregado == False and valido == True :
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
                print(obj_almacen.agregado)
                obj_almacen.save()
                #nombre = 
                return Response ({'SUCCESS':'AGREGADO'})
                    
            elif agregado == True:
                return Response({'ERROR':'PRODUCTO YA AGREGADO AL ALMACEN'})   



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
"""
