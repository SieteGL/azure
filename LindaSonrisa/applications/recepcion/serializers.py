from rest_framework import serializers, pagination
#
from .models import Orden, Detalles, Estado, Recepcion
#
#from applications.users.models import User
from rest_framework.validators import UniqueValidator


class DetallesSerializers(serializers.Serializer):
    #pk = serializers.IntegerField() 
    cantidad = serializers.IntegerField() 
    precio_unitario = serializers.IntegerField()
    nombre_producto = serializers.CharField()
    familia = serializers.CharField()
    descripcion = serializers.CharField()
    fecha_vencimiento=serializers.CharField()
    proveedor = serializers.EmailField()

#validando que el nombre de la orden sea unico.
class OrdenesSerializer(serializers.Serializer):
    name = serializers.CharField(validators=[UniqueValidator(queryset=Orden.objects.all())])
    #proveedor = serializers.EmailField()
    #model Detalle
    detalle = DetallesSerializers(many=True)

class ActualizarAlmacen(serializers.Serializer):
    pk = serializers.IntegerField() 
    

class RecepcionSerializer(serializers.Serializer):
    detalle = ActualizarAlmacen(many=True)
#   

#serializar Orden
class OrdenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orden
        fields = ('name',)  

class DetallesSerializer(serializers.ModelSerializer):
    ordenes = OrdenSerializer()
    class Meta:
        model = Detalles
        fields = ( 
            'id',
            'ordenes',
            'nombre_producto',
            'descripcion',
            'cantidad',
            'precio_unitario',
            'total'
        )
        


#Serializar estados 
class EstadosSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Estado
        fields = ('__all__') 

class EstadoSerializer(serializers.Serializer):
    orden = OrdenSerializer()
    proveedores = serializers.CharField()
    estados = serializers.IntegerField()
    Observaciones = serializers.CharField()


