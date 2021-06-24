from django.utils import timezone
from datetime import datetime
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
)
#
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import  IsAuthenticated, IsAdminUser
from django.shortcuts import render
#
from rest_framework.response import Response

from .models import Boleta, BoletaServicio
from applications.boleta.models import Almacen
from applications.configuracion.models import Empresa
from applications.servicios.models import Servicios

from .serializers import (
    Boletaserializer, 
    BoletaRegistroSerializer ,
    #probando con el de abajo  
    BoletaAlmacenSerializer,
    
    )
from .managers import BoletaManager
#from LindaSonrisa.applications.boleta import serializers




#LISTAR TODAS LAS BOLETAS MEDIANTE ALGUN FILTRO EN ESPECIFICO
class ListBoletaUser(ListAPIView):
   
    #authentication_classes = (TokenAuthentication, )
    
    #permission_classes = [IsAuthenticated]

    serializer_class = Boletaserializer
    def get_queryset(self):
        usuario = self.request.user
        
        return Boleta.objects.all()
        #return Boleta.objects.boletas_por_usuario(usuario)

"""
class CreateBoletaUser(CreteAPIView):
    serializer_class = """



#CREAR BOLETA PARA QUE EL CLIENTE REALICE EL PAGO DE SU CONSULTA REALIZANDO EL RECARGO DE SERVICIO, DESCUENTOS DE PACIENTE.

class CreateBoletaUser(CreateAPIView):

    serializer_class = BoletaAlmacenSerializer

    def create(self, request, *args, **kwargs):
        #desiarilizando informacion desde json con formato requerido
        serializer = BoletaAlmacenSerializer(data=request.data)
        #verificar informar si cumple formato... validación OJO
        serializer.is_valid(raise_exception=True)
        #validando
        invoce = Boleta.objects.create(
            empresa = Empresa.objects.all(),
            cliente = self.request.user,
        )
        #variables para el calculo
        valor_unitario = 0
        cantidad = 0
        valor_total = 0
        #recuperamos los detalles de la boleta
        #buscar por pk de detalles 'OK' detalles_boleta = serializer.validate_data['detalle']
        #
        almacen = serializer.validate_data['almacen']
        #se crea arreglo para guardas datos
        boleta_detalle = []

        for store in almacen:
            #se recupera el id del producto del almacen
            alma = Almacen.objects.get(id=store['pk'])
            boleta_detallada = BoletaServicio(
                boleta = invoce,
                almacen = alma,
                cantidad = serializer.validated_data['cantidad'],
                #cantidad = store['valor_unitario'],
                valor_total = serializer.validated_data['valor_total'],
                fecha_atencion = timezone.now(),
            )
            #multiplicando cantidad * valor en el ALMACEN models
            valor_total = cantidad * store['valor_unitario']
            #reduciendo el stock del almacen            
            alma['stock'] = alma['stock'] - cantidad
            #
            boleta_detalle.append(boleta_detallada)
        #
        #le damos los valores
        #valor total a la boleta
        boleta_detallada.valor_total = valor_total
        #actualizamos el almacen
        alma['stock'] = alma['stock']
        boleta_detallada.save()
        #
        BoletaServicio.objects.bulk_create(boleta_detalle)
        #retorno
        return Response({'msj':'Agregado con exito'})





















        boleta_detalles = []
        # revisar si guarda los valores en sistema
        detalle_boleta = BoletaServicio(
            valor_unitario=valor_unitario,
            cantidad=cantidad['cantidad'],
            #valor_total=valor_total,
            fecha_atencion=timezone.now()
        )
        total = cantidad * valor_unitario


"""
class CreateBoleta(CreateAPIView):
    serializer_class = asd    

    def create(self, request, *args, **kwargs):
        serializer = asd(data=request.data)
        serializer.is_valid(raise_exception=True)
        asds = Servicios.objects.all()


        #recuperar valores de     
"""

#ACTUALIZAR ALGUNA BOLETA SI ES NECESARIO A FUTURO, PUEDE SER PARA NO CREAR UNA DESDE CERO O SIMPLEMENTE ACTUALIZACION A FUTURO

#ELIMINAR UNA BOLETA MEDIANTE ALGUN IDENTIFICADOR UNICO DEL SISTEMA COMO POR EJEMPLO EL RUN DEL PACIENTE.