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
from .serializers import AlmacenSerializers, ActualizarSerializer

from .models import Almacen
from applications.recepcion.models import Detalles


class ListarAlmacen(ListAPIView):
    serializer_class = AlmacenSerializers

    def get_queryset(self):
        usuario = self.request.user
        #modificar para email o por tipo_usuario
        return Almacen.objects.almacen_por_email(usuario)

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

    
             