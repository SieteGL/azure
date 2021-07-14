from rest_framework import serializers, pagination
#

#
from .models import BoletaServicio, Boleta
# model de un 3ro
from applications.servicios.models import Servicios

#Serializadores para el ListPorCliente
class ServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servicios
        fields = ('id','servicio')

#modelos para listar boletas
class Boletaserializer(serializers.ModelSerializer):    
    #bien
    detalle = serializers.SerializerMethodField()
    class Meta:
        model = Boleta
        fields = (
            'id',
            'empresa',#bueno
            'cliente',#bueno
            'serviciosList',#bueno
            'detalle'
        )
    
    # def get_detalle(self, obj):        
    #     query = BoletaServicio.objects.boletas_por_usuario(obj.cliente)
    #     boletaF_serializada = BoletaServicioSerializer(query, many=True).data
    #     return boletaF_serializada      

class BoletaServicioSerializer(serializers.ModelSerializer):    
    
    class Meta:
        model = BoletaServicio
        fields = (       
            'id',     
            #'valor_unitario',
            'cantidad',
            'valor_total',
            'fecha_atencion',
            #'serviciosLista',
            'boleta',                   
        )


# #estos 2 van juntos son de prueba 48 a las 56   
# class DetallesSerializers(serializers.ModelSerializer):

#     pk = serializers.IntegerField()
# class BoletaRegistroSerializer(serializers.ModelSerializer):

#     valor_unitario =  serializers.IntegerField()
#     cantidad = serializers.IntegerField()
#     valor_total = serializers.IntegerField()
#     detalle = DetallesSerializers(many=True)


# #pruebas para serializers almacen con boleta para realizar cambios en el almacen y generar boleta

# class AlmacenDetailSerializer(serializers.Serializer):
#     pk = serializers.IntegerField()
#     valor_unitario = serializers.IntegerField()
#     stock = serializers.IntegerField()
#     stock_critico = serializers.IntegerField()


# class BoletaAlmacenSerializer(serializers.Serializer):

#     cantidad = serializers.IntegerField()
#     valor_total = serializers.IntegerField()
#     boleta = BoletaServicioSerializer
#     almacen = AlmacenDetailSerializer(many=True)



# #########

# #traer informacion de almacen
# class AlmacenSerializer(serializers.Serializer):
#     codigo = serializers.IntegerField()
#     stock = serializers.IntegerField()
#     stock_critico = serializers.IntegerField()
#     valor_unitario = serializers.IntegerField()



class DatosSerializers(serializers.Serializer):
    #PK de servicios, user, documentos,
    empresa = serializers.IntegerField()
    servicios = serializers.IntegerField()
    documento = serializers.IntegerField()
    cliente = serializers.IntegerField()
    especialista = serializers.IntegerField()
    #almacen = serializers.IntegerField()

class BoletaSerializer(serializers.Serializer):
    datos = DatosSerializers(many=True)
    