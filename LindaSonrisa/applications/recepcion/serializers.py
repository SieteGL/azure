from rest_framework import serializers, pagination
from rest_framework.fields import BooleanField
#
from .models import Orden, Detalles, Estado, Recepcion
#
#from applications.users.models import User
from rest_framework.validators import UniqueValidator


class DetallesSerializers(serializers.Serializer):    
    cantidad = serializers.IntegerField() 
    precio_unitario = serializers.IntegerField()
    nombre_producto = serializers.CharField()
    familia = serializers.CharField()
    descripcion = serializers.CharField()
    fecha_vencimiento=serializers.CharField(required=False, allow_null=True)        
    pk = serializers.IntegerField()
    #recepcionado = BooleanField()


#validando que el nombre de la orden sea unico.
class OrdenessSerializer(serializers.Serializer):
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
        fields = ('id','name',)  

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
            'total',
            'valid'
        )
        
class RecepcionSerializer(serializers.ModelSerializer):
    detalles_recepcion = DetallesSerializer()
    class Meta:
        model = Recepcion
        fields = (
            'id',
            'receptor',
            'detalles_recepcion',
            'valido'
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



class ReceptorSerializer(serializers.Serializer):
    # valido = serializers.BooleanField()
    # agregado = serializers.BooleanField()
    detalles = ActualizarAlmacen(many=True)


class OrdenPKSerializers(serializers.Serializer):
    pk = serializers.IntegerField()

class ActualizarSerializer(serializers.Serializer):
    ordenes = OrdenPKSerializers(many=True)
    estados = serializers.CharField()
    observacion = serializers.CharField()


class DetallesProveedor(serializers.ModelSerializer):
    #ordenes = OrdenSerializer()
    class Meta:
        model = Detalles
        fields = ( 
            'id',
            'codigo',
            'proveedor',
        )    


class OrdenesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orden
        fields = ('__all__')  

class DetalleSerializer(serializers.ModelSerializer):
    ordenes = OrdenesSerializer()
    class Meta:
        model = Detalles
        fields = ( 
            'ordenes',
            'id',
            'codigo',                     
            'nombre_producto',
            'familia',            
            'descripcion',
            'fecha_vencimiento',
            'cantidad',
            'precio_unitario',
            'total',
            'proveedor',
            'valid',
            'recepcionado'
        )        