#
#from re import S
from applications.users.permissions import IsEmployeeUser
from django.utils import timezone
from datetime import datetime

from django.shortcuts import render
from rest_framework import serializers
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
# response
from rest_framework.response import Response
# Vistasf
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    UpdateAPIView,
    DestroyAPIView
)
# serializadores
from .serializers import (
    OrdenesSerializer,
    EstadoSerializer,
    DetallesSerializer,
    OrdenSerializer,
    EstadosSerializer,
    RecepcionSerializer,    
    ReceptorSerializer,
    ActualizarSerializer,
    DetallesProveedor,
    DetalleSerializer,
    OrdenessSerializer
)


# models
from .models import (
    Orden,
    Detalles,
    Estado,
    Recepcion
)
# models otras app's
from applications.almacen.models import Almacen
from applications.users.models import User

from applications.users.permissions import IsClienteUser, IsSupplierUser


# managers
#from .managers import ConsultasManager
# ORDENES CREADAS POR EL EMPLEADO PARA QUE QUEDE REGISTRO DE LO SOLICITADO AL PROVEEDOR Y
# ASI PODER REALIZAR ACTUALIZACION DE ALMACEN CUANDO EL PRODUCTO SEA RECEPCIONADO Y VALIDADO

#Crear orden y detalles del pedido
class CrearPedido(CreateAPIView):
    serializer_class = OrdenessSerializer

    def create(self, request, *args, **kwargs):
        serializer = OrdenessSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        tot = 0
        # afuera el que no tiene la relacion
        orden = Orden.objects.create(
            fecha=timezone.now(),
            name=serializer.validated_data['name'],
            recepcion=self.request.user,
        )
        list_detalles = []
        code = '0'

        #--------------------------------------------------#
        detalles_query = Detalles.objects.all()
        codig = 'a'
        # if detalles_query != None:
        #     for detail_query in detalles_query:
        #         codig = detail_query.nombre_producto
        # else:
        #     codig = 'a'
        # for detail_query in detalles_query:
        #     codig = detail_query.nombre_producto

        detalles = serializer.validated_data['detalle']

        for details in detalles:
            # Se espera el valor del proveedor ID de este. para poder guardar quien fue
            # el que trajo los productos
            id_proveedor = User.objects.get(id=details['pk'])
            tot = details['cantidad']*details['precio_unitario']

            # PRIMEROS 3 DIGITOS
            print(id_proveedor)
            r = id_proveedor.rut[0:1]
            c = id_proveedor.email[0:1]
            n = id_proveedor.nombre[0:1]
            #
            familia = details['familia']
            familia = familia[0:3]
            #
            vencimiento = details['fecha_vencimiento']
            #vence = datetime.strptime(vencimiento, '%Y/%m/%d')
            # ahora = datetime.now()
            # ahora = ahora.date()
            # ahora = ahora.strftime('%Y-%m-%d')
            # print(vencimiento)
            # print('espacio')
            # print(ahora)
            ahora = '2099-12-31'
            #si fecha de vencimiento es igual a hoy quiere decir que no vence.
            #y quiere decir que no vence
            if vencimiento != ahora:
                año = vencimiento[0:4]
                mes = vencimiento[5:7]
                dia = vencimiento[8:10]
                code = r+c+n+familia+dia+mes+año
                code = code.lower()
            else:
                no_fecha = '00000000'
                code = r+c+n+familia+no_fecha
                code = code.lower()

            # print('nuevo'+codig)
            #if codig != details['nombre_producto']:
                
            detalles = Detalles(
                ordenes=orden,
                codigo=code,
                nombre_producto=details['nombre_producto'],
                familia=details['familia'],
                descripcion=details['descripcion'],
                fecha_vencimiento=details['fecha_vencimiento'],
                cantidad=details['cantidad'],
                precio_unitario=details['precio_unitario'],
                total=tot,
                proveedor=id_proveedor,
                valid='1',
                recepcionado=False
            )
            list_detalles.append(detalles)
        Detalles.objects.bulk_create(list_detalles)                
        return Response({'SUCCESS': 'OBJECTO CREADO CON EXITO'})
            # else:
            #     det = Detalles.objects.all()
            #     for d in det:
            #         print(det)
            #         if d.nombre_producto == codig and d.precio_unitario == details['precio_unitario']:
            #             d.ordenes = orden
            #             d.cantidad = d.cantidad + details['cantidad']
            #             d.total = d.total + (details['cantidad'] * details['precio_unitario'])
            #             d.save() 
            #             print(d.cantidad)
            #     print('wena choro')
            #    return Response({'SUCCESS': 'OBJECTO ACTUALIZADO CON EXITO'})

class ListRecepcion(ListAPIView):
    serializer_class = RecepcionSerializer
    def get_queryset(self):                       
        return Recepcion.objects.all()


class CrearRecepcion(CreateAPIView):
    serializer_class = ReceptorSerializer

    def create(self, request,*args, **kwargs):
        serializer = ReceptorSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        list_recepcion = []

        details = serializer.validated_data['detalles']

        for detalles in details:
            #Orden no detalles
            #revisar si esta bien porque quiero revisar por cada uno si los productos son correctos
            #no la orden en si; Si no ver si lo que estoy recibiendo a detalle (mninucioso) es correcto
            id_detalles = Detalles.objects.get(id=detalles['pk'])

            recepcion = Recepcion(
                receptor = self.request.user,
                #cambiar a Orden
                detalles_recepcion = id_detalles,
                valido = True,
                agregado = False
            )
            list_recepcion.append(recepcion)
            
            #
            id_detalles.valid=False
            id_detalles.recepcionado=True
            id_detalles.save()
                #despues de agregar la recepcion, se realiza la actualizacion del
                #estado en Detalles de recepcionado e is_valid(choices)
                #ademas se cambia el valido de recepcion para decir que es valido y poder
                #agregarlo al almacen.
                #y luego realizar el cambio de estado y no poder listarlo mas y no sea 
                #agregado al almacen de nuevo

                #Pensar que si necesito con urgencia 1 producto lo puedo aceptar, sin aceptar los demas 
                # y poder atender un paciente si es nececsario
        # if id_detalles.recepcionado != True:
        Recepcion.objects.bulk_create(list_recepcion)
        
        
        return Response({'SUCCESS':'PRODUCTOS RECEPCIONADOS CON EXITO'})    


class ActualizarEstado(CreateAPIView):
    serializer_class = ActualizarSerializer
    
    def create(self, request, *args, **kwargs):
        serializer = ActualizarSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        estado_list = []
        actualizacion = serializer.validated_data['ordenes']

        for act in actualizacion:
            order = Orden.objects.get(id=act['pk'])

            estado = Estado(
                orden = order,
                proveedores = self.request.user,                
                estados = serializer.validated_data['estados'],
                observacion = serializer.validated_data['observacion']
            )
            estado_list.append(estado)
        Estado.objects.bulk_create(estado_list)
        return Response({'SUCCES': 'ACTUALIZACION COMPLETA'})


#Devuelve los detalles por proveedor, para resivir pk 
class ListOrdenesProveedores(ListAPIView):
    serializer_class = DetallesProveedor
    def get_queryset(self):    
        user = self.request.user   
        return Detalles.objects.ordenes_por_proveedor(user)


class ListDetalles(ListAPIView):
    serializer_class = DetalleSerializer
    def get_queryset(self):
        return Detalles.objects.all()




















#-----------------------------------------------#

# combinar la creacion de #Orden mas #Detalles
"""class CrearOrdenPedidos(CreateAPIView):
    permission_classes = [IsAuthenticated, IsAdminUser]

    serializer_class = OrdenesSerializer

    def create(self, request, *args, **kwargs):
        serializer = OrdenesSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        tot = 0
        # afuera el que no tiene la relacion
        orden = Orden.objects.create(
            fecha=timezone.now(),
            name=serializer.validated_data['name'],
            recepcion=self.request.user,
            # mover proveedor a detalles y dejarlo mejor por dentro y no agregar correo
            # de forma manual
            # proveedor=serializer.validated_data['proveedor']
        )
        list_detalles = []

        # linea agregada para entrar a Detalles.models.py
        detalles = serializer.validated_data['detalle']

        for det in detalles:
            id_proveedor = det['proveedor']
            id_proveedor = id_proveedor[0:3]

            familia_id = det['familia']
            familia_id = familia_id[0:3]

            fecha_ids = det['fecha_vencimiento']

            #fecha_idss = fecha_ids.strftime("%d%m%Y")
            # falta revisar como dejar un campo fecha vacio mediante serializer
            if len(fecha_ids) > 8:
                print(fecha_ids, familia_id, id_proveedor)
                code = id_proveedor + familia_id + "00000000" + "asd"
            else:
                code = id_proveedor + familia_id + fecha_ids + "asd"

            tot = det['cantidad']*det['precio_unitario']
            # detalles tiene orden
            deta = Detalles(
                ordenes=orden,
                codigo=code,
                nombre_producto=det['nombre_producto'],
                familia=det['familia'],
                descripcion=det['descripcion'],
                fecha_vencimiento=det['fecha_vencimiento'],
                cantidad=det['cantidad'],
                precio_unitario=det['precio_unitario'],
                total=tot,
                proveedor=det['proveedor']
            )
            list_detalles.append(deta)
        Detalles.objects.bulk_create(list_detalles)
        list_detalles.clear()
        return Response({'res': 'ok'})"""

# Listar por nombre de la orden, de Orden listo


class ListOrdenPedidos(ListAPIView):
    permission_classes = [IsAuthenticated, IsAdminUser| IsEmployeeUser]
    serializer_class = DetallesSerializer

    def get_queryset(self):
        nombre = self.kwargs['nombre']
        return Detalles.objects.orden_numero(nombre)


# falta por terminar y revisar informacion
class UpdateEstado(CreateAPIView):

    permission_classes = [IsAuthenticated, IsSupplierUser, ]
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
                    cantidad=details.cantidad,
                    precio_unitario=details.precio_unitario,
                    # detalles_recepcion=details,
                    almacen=details.almacen
                )
                lista_recepcion.append(reception)
                Almacen.objects.bulk_create(lista_recepcion)
        return Response({'res': 'ok'})


# ESTADO PROVEEDOR TIENE ACCESO A ESTA SECCION PARA DECIR EN QUE ESTAN LOS PEDIDOS NECESARIOS
