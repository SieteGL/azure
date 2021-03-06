
from django.utils import timezone
from datetime import datetime, time
from rest_framework import serializers
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
)
#
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.shortcuts import render
#
from rest_framework.response import Response

from .models import Boleta, BoletaServicio
from applications.boleta.models import Almacen
from applications.configuracion.models import Empresa
from applications.servicios.models import Servicios
from applications.documentos.models import Documento
from applications.users.models import User

from .serializers import (
    BoletaSerializer,
    BoletaServicioSerializer,
    Boletaserializers,
    PaginationSerializer

)
from .managers import BoletaManager
#from LindaSonrisa.applications.boleta import serializers

class ListBoletaFiltro(ListAPIView):
    serializer_class = BoletaServicioSerializer

    def get_queryset(self):        
        rut = self.request.query_params.get('rut', None)
        if rut is None:
            return BoletaServicio.objects.all()
        if rut is not None:
            return BoletaServicio.objects.boleta_rut(
               rut=rut 
            )            


class CrearBoleta(CreateAPIView):
    serializer_class = BoletaSerializer

    def create(self, request, *args, **kwargs):
        serializer = BoletaSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        dscto = 0
        boleta_numero=0
        boleta_lista = []
        serverces = serializer.validated_data['servicios']

        boleta = serializer.validated_data['datos']

        for boletas in boleta:

            empresa = Empresa.objects.get(id=boletas['empresa'])
            #servicios = Servicios.objects.get(id=boletas['servicios'])
            documento = Documento.objects.get(id=boletas['documento'])
            cliente = User.objects.get(id=boletas['cliente'])
            especialista = User.objects.get(id=boletas['especialista'])
            #almacen = Almacen.objects.get(id=boletas['almacen'])

            tipo_documento = documento.documento
            valor_documento = documento.valor
# cabecera  
            numero = 0
            
            bolet = Boleta.objects.filter().last()
            if bolet is not None:                
                numero = bolet.boleta_numero
                numero += 1

            print(numero)
            if tipo_documento == '0':
                if valor_documento >= 0 and valor_documento <= 350000:
                    # porcentaje para calculos
                    dscto = 50
                    invoce = Boleta.objects.create(
                        boleta_numero=numero,
                        fecha_atencion=timezone.now(),
                        empresa=empresa,
                        cliente=cliente,
                        documento=tipo_documento,
                        descuento=dscto
                    )
                    invoce.save()
                elif valor_documento >= 350000 and valor_documento <= 600000:
                    dscto = 35
                    invoce = Boleta.objects.create(
                        boleta_numero=numero,
                        fecha_atencion=timezone.now(),
                        empresa=empresa,
                        cliente=cliente,
                        documento=tipo_documento,
                        descuento=dscto
                    )
                    invoce.save()
                elif valor_documento >= 600000 and valor_documento <= 900000:
                    dscto = 20
                    invoce = Boleta.objects.create(
                        boleta_numero=numero,
                        fecha_atencion=timezone.now(),
                        empresa=empresa,
                        cliente=cliente,
                        documento=tipo_documento,
                        descuento=dscto
                    )
                    invoce.save()
                elif valor_documento >= 900000 and valor_documento <= 1250000:
                    dscto = 5
                    invoce = Boleta.objects.create(
                        boleta_numero=numero,
                        fecha_atencion=timezone.now(),
                        empresa=empresa,
                        cliente=cliente,
                        documento=tipo_documento,
                        descuento=dscto
                    )
                    invoce.save()
            elif tipo_documento == '1':
                if valor_documento >= 0 and valor_documento <= 300000:
                    # porcentaje para calculos
                    dscto = 85
                    invoce = Boleta.objects.create(
                        boleta_numero=numero,
                        fecha_atencion=timezone.now(),
                        empresa=empresa,
                        cliente=cliente,
                        documento=tipo_documento,
                        descuento=dscto
                    )
                    invoce.save()
                elif valor_documento >= 300000 and valor_documento <= 600000:
                    dscto = 50
                    invoce = Boleta.objects.create(
                        boleta_numero=numero,
                        fecha_atencion=timezone.now(),
                        empresa=empresa,
                        cliente=cliente,
                        documento=tipo_documento,
                        descuento=dscto
                    )
                    invoce.save()
                elif valor_documento >= 600000 and valor_documento <= 900000:
                    dscto = 35
                    invoce = Boleta.objects.create(
                        boleta_numero=numero,
                        fecha_atencion=timezone.now(),
                        empresa=empresa,
                        cliente=cliente,
                        documento=tipo_documento,
                        descuento=dscto
                    )
                    invoce.save()
                elif valor_documento >= 900000 and valor_documento <= 1250000:
                    dscto = 5
                    invoce = Boleta.objects.create(
                        boleta_numero=numero,
                        fecha_atencion=timezone.now(),
                        empresa=empresa,
                        cliente=cliente,
                        documento=tipo_documento,
                        descuento=dscto
                    )
                    invoce.save()
            elif tipo_documento == '2':
                if valor_documento >= 0 and valor_documento <= 50000:
                    # porcentaje para calculos
                    dscto = 50
                    invoce = Boleta.objects.create(
                        boleta_numero=numero,
                        fecha_atencion=timezone.now(),
                        empresa=empresa,
                        cliente=cliente,
                        documento=tipo_documento,
                        descuento=dscto
                    )
                    invoce.save()
                elif valor_documento >= 50000 and valor_documento <= 75000:
                    dscto = 35
                    invoce = Boleta.objects.create(
                        boleta_numero=numero,
                        fecha_atencion=timezone.now(),
                        empresa=empresa,
                        cliente=cliente,
                        documento=tipo_documento,
                        descuento=dscto
                    )
                    invoce.save()
                elif valor_documento >= 75000 and valor_documento <= 90000:
                    dscto = 20
                    invoce = Boleta.objects.create(
                        boleta_numero=numero,
                        fecha_atencion=timezone.now(),
                        empresa=empresa,
                        cliente=cliente,
                        documento=tipo_documento,
                        descuento=dscto
                    )
                    invoce.save()
                elif valor_documento >= 90000 and valor_documento <= 110000:
                    dscto = 5
                    invoce = Boleta.objects.create(
                        boleta_numero=numero,
                        fecha_atencion=timezone.now(),
                        empresa=empresa,
                        cliente=cliente,
                        documento=tipo_documento,
                        descuento=dscto
                    )
                    invoce.save()

        # for
    # def   
            
            total=0
            totals=0
            sub=0
            b=0
            # block descuento
            # revisar bloque completo
            for servs in serverces:
                servicios = Servicios.objects.get(id=servs['pk'])
                sub += servicios.valor_paquete 
                #sub += sub
                print(sub)
                a = servicios.valor_paquete*dscto
                b = a / 100
                print('descuento')
                print(dscto)
                total = servicios.valor_paquete - b
                totals += total
            
            # end block descuento
                boleta_servicio = BoletaServicio(
                    boleta=invoce,
                    especialista=especialista,
                    sub_total=sub,
                    total=totals
                )
            #bueno se guarda una vez
            boleta_servicio.save()
            servicios = Servicios.objects.get(id=servs['pk'])
            boleta_servicio.serviciosList.add(servicios)
            
            # boleta_servicio.save()
        return Response({'success': 'funciona'})


class ListBoleta(ListAPIView):
    pagination_class = PaginationSerializer
    serializer_class=BoletaServicioSerializer
    
    def get_queryset(self):
        return BoletaServicio.objects.all()

class ListBoletaUser(ListAPIView):
    pagination_class = PaginationSerializer
    serializer_class=BoletaServicioSerializer

    def get_queryset(self):
        valor = self.kwargs['pk']
        return BoletaServicio.objects.boleta_por_cliente(valor)






# #LISTAR TODAS LAS BOLETAS MEDIANTE ALGUN FILTRO EN ESPECIFICO
# class ListBoletaUser(ListAPIView):

#     authentication_classes = (TokenAuthentication, )

#     permission_classes = [IsAuthenticated]

#     serializer_class = Boletaserializer
#     def get_queryset(self):
#         usuario = self.request.user

#         return Boleta.objects.all()
#         #return Boleta.objects.boletas_por_usuario(usuario)

#
# class CreateBoletaUser(CreteAPIView):
#     serializer_class = """


# #CREAR BOLETA PARA QUE EL CLIENTE REALICE EL PAGO DE SU CONSULTA REALIZANDO EL RECARGO DE SERVICIO, DESCUENTOS DE PACIENTE.

# class CreateBoletaUser(CreateAPIView):

#     serializer_class = BoletaAlmacenSerializer

#     def create(self, request, *args, **kwargs):
#         #desiarilizando informacion desde json con formato requerido
#         serializer = BoletaAlmacenSerializer(data=request.data)
#         #verificar informar si cumple formato... validaci??n OJO
#         serializer.is_valid(raise_exception=True)
#         #validando
#         invoce = Boleta.objects.create(
#             empresa = Empresa.objects.all(),
#             cliente = self.request.user,
#         )
#         #variables para el calculo
#         valor_unitario = 0
#         cantidad = 0
#         valor_total = 0
#         #recuperamos los detalles de la boleta
#         #buscar por pk de detalles 'OK' detalles_boleta = serializer.validate_data['detalle']
#         #
#         almacen = serializer.validate_data['almacen']
#         #se crea arreglo para guardas datos
#         boleta_detalle = []

#         for store in almacen:
#             #se recupera el id del producto del almacen
#             alma = Almacen.objects.get(id=store['pk'])
#             boleta_detallada = BoletaServicio(
#                 boleta = invoce,
#                 almacen = alma,
#                 cantidad = serializer.validated_data['cantidad'],
#                 #cantidad = store['valor_unitario'],
#                 valor_total = serializer.validated_data['valor_total'],
#                 fecha_atencion = timezone.now(),
#             )
#             #multiplicando cantidad * valor en el ALMACEN models
#             valor_total = cantidad * store['valor_unitario']
#             #reduciendo el stock del almacen
#             alma['stock'] = alma['stock'] - cantidad
#             #
#             boleta_detalle.append(boleta_detallada)
#         #
#         #le damos los valores
#         #valor total a la boleta
#         boleta_detallada.valor_total = valor_total
#         #actualizamos el almacen
#         alma['stock'] = alma['stock']
#         boleta_detallada.save()
#         #
#         BoletaServicio.objects.bulk_create(boleta_detalle)
#         #retorno
#         return Response({'msj':'Agregado con exito'})


# """


#         boleta_detalles = []
#         # revisar si guarda los valores en sistema
#         detalle_boleta = BoletaServicio(
#             valor_unitario=valor_unitario,
#             cantidad=cantidad['cantidad'],
#             #valor_total=valor_total,
#             fecha_atencion=timezone.now()
#         )
#         total = cantidad * valor_unitario


# """
# class CreateBoleta(CreateAPIView):
#     serializer_class = asd

#     def create(self, request, *args, **kwargs):
#         serializer = asd(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         asds = Servicios.objects.all()


#         #recuperar valores de
# """

# #ACTUALIZAR ALGUNA BOLETA SI ES NECESARIO A FUTURO, PUEDE SER PARA NO CREAR UNA DESDE CERO O SIMPLEMENTE ACTUALIZACION A FUTURO

# #ELIMINAR UNA BOLETA MEDIANTE ALGUN IDENTIFICADOR UNICO DEL SISTEMA COMO POR EJEMPLO EL RUN DEL PACIENTE.
