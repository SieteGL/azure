#
#from re import S
from applications.users.permissions import IsEmployeeUser
from django.utils import timezone
from datetime import datetime

from django.shortcuts import render
from rest_framework import serializers
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import  IsAuthenticated, IsAdminUser
#response
from rest_framework.response import Response
#Vistas
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    UpdateAPIView,
    DestroyAPIView
)
#serializadores
from .serializers import (
    OrdenesSerializer,
    EstadoSerializer,
    DetallesSerializer,
    OrdenSerializer,
    EstadosSerializer,
    RecepcionSerializer
)
#models
from .models import (
    Orden,
    Detalles,
    Estado,
    Recepcion
)
#models otras app's
from applications.almacen.models import Almacen
from applications.users.models import User

from applications.users.permissions import IsClienteUser, IsSupplierUser


#managers
#from .managers import ConsultasManager
#ORDENES CREADAS POR EL EMPLEADO PARA QUE QUEDE REGISTRO DE LO SOLICITADO AL PROVEEDOR Y
# ASI PODER REALIZAR ACTUALIZACION DE ALMACEN CUANDO EL PRODUCTO SEA RECEPCIONADO Y VALIDADO


#combinar la creacion de #Orden mas #Detalles
class CrearOrdenPedidos(CreateAPIView):
    permission_classes = [IsAuthenticated, IsEmployeeUser, IsAdminUser] 

    serializer_class = OrdenesSerializer

    def create(self, request, *args, **kwargs):
        serializer = OrdenesSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)        
        tot = 0
        #afuera el que no tiene la relacion
        orden = Orden.objects.create(
            fecha=timezone.now(),
            name=serializer.validated_data['name'],
            recepcion=self.request.user,
            #mover proveedor a detalles y dejarlo mejor por dentro y no agregar correo
            #de forma manual
            #proveedor=serializer.validated_data['proveedor'] 
        )        
        list_detalles = []
         
        #linea agregada para entrar a Detalles.models.py        
        detalles = serializer.validated_data['detalle']

        for det in detalles:
            id_proveedor=det['proveedor']
            id_proveedor=id_proveedor[0:3]

            familia_id = det['familia']
            familia_id = familia_id[0:3]

            fecha_ids = det['fecha_vencimiento']
            
            fecha_idss = fecha_ids.strftime("%d%m%Y")                             
            #falta revisar como dejar un campo fecha vacio mediante serializer
            if len(fecha_idss) > 8:
                print(fecha_idss,familia_id,id_proveedor)
                code = id_proveedor + familia_id + "00000000" + "asd"
            else:
                code = id_proveedor + familia_id + fecha_idss + "asd"                    
            
            tot = det['cantidad']*det['precio_unitario']
            #detalles tiene orden
            deta = Detalles(
                ordenes=orden,
                codigo = code,
                nombre_producto=det['nombre_producto'],
                familia = det['familia'],
                descripcion=det['descripcion'],
                fecha_vencimiento = det['fecha_vencimiento'],
                cantidad=det['cantidad'],
                precio_unitario=det['precio_unitario'],                
                total=tot,
                proveedor = det['proveedor']
            )
            list_detalles.append(deta)
        Detalles.objects.bulk_create(list_detalles)
        list_detalles.clear()
        return Response({'res': 'ok'})        

#Listar por nombre de la orden, de Orden listo 
class ListOrdenPedidos(ListAPIView):
    permission_classes = [IsAuthenticated, IsAdminUser, IsEmployeeUser] 
    serializer_class = DetallesSerializer

    def get_queryset(self):
        nombre = self.kwargs['nombre']        
        return Detalles.objects.orden_numero(nombre)



#falta por terminar y revisar informacion
class UpdateEstado(CreateAPIView):
    
    permission_classes = [IsAuthenticated, IsSupplierUser,]
    serializer_class = EstadosSerializer

    def get_queryset(self):
        user = self.request.user
        Estado.objects.estado_por_proveedor(user)
        return  

######################################################
class RevisarRecepcionAlmacen(CreateAPIView):
    serializer_class = RecepcionSerializer

    def create(self, request, *args, **kwargs):
        serializer = RecepcionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)  

        
        detalles = serializer.validated_data['detalle']

        lista_recepcion = []
        for dtl in detalles:

            details = Detalles.objects.get(id=dtl['pk'])
            

            validaciones = details.valid = True

            if validaciones == True:  
                reception = Detalles(
                    ordenes=details.recepcion,
                    cantidad = details.cantidad,
                    precio_unitario = details.precio_unitario,
                    #detalles_recepcion=details,                             
                    almacen = details.almacen
                )
                lista_recepcion.append(reception)
                Almacen.objects.bulk_create(lista_recepcion)
        return Response({'res': 'ok'}) 



#ESTADO PROVEEDOR TIENE ACCESO A ESTA SECCION PARA DECIR EN QUE ESTAN LOS PEDIDOS NECESARIOS