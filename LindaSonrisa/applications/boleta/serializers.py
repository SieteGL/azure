from rest_framework import serializers, pagination
#

#
from .models import BoletaServicio, Boleta
# model de un 3ro
from applications.servicios.models import Servicios
#terceros models
from applications.users.models import User
#
from applications.configuracion.models import Empresa

class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        fields = '__all__'

#Serializadores para el ListPorCliente
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class ServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servicios
        fields = '__all__'

#modelos para listar boletas
class Boletaserializers(serializers.ModelSerializer):    
    
    cliente = UserSerializer()
    empresa = EmpresaSerializer()
    class Meta:
        model = Boleta
        fields = '__all__'
        
class BoletaServicioSerializer(serializers.ModelSerializer):    

    boleta = Boletaserializers()
    serviciosList = ServicesSerializer(many=True)
    especialista = UserSerializer()
    class Meta:
        model = BoletaServicio
        fields = (       
            'id',     
            'boleta',
            'serviciosList',
            'especialista',
            'sub_total', 
            'total'         
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

class PKSerializers(serializers.Serializer):
    pk = serializers.IntegerField()

class DatosSerializers(serializers.Serializer):
    #PK de servicios, user, documentos,
    empresa = serializers.IntegerField()
    # servicios = serializers.IntegerField()
    documento = serializers.IntegerField()
    cliente = serializers.IntegerField()
    especialista = serializers.IntegerField()
    #almacen = serializers.IntegerField()

class BoletaSerializer(serializers.Serializer):
    datos = DatosSerializers(many=True)
    servicios = PKSerializers(many=True)

class PaginationSerializer(pagination.PageNumberPagination):
    page_size = 3
    max_page_size = 25   