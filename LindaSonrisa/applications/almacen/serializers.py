from rest_framework import serializers, pagination
#
from .models import Almacen, Familia

class AlmacenSerializers(serializers.ModelSerializer):
 
    class Meta:
        model = Almacen
        fields = '__all__'



# class ActualizarAlmacen(serializers.Serializer):
#     pk = serializers.IntegerField() 
    

# class ActualizarSerializer(serializers.Serializer):
#     #ejemplo =  AlmacenSerializers()   
#     valido = serializers.BooleanField()
#     detalless = ActualizarAlmacen(many=True)
  

class OrdenSerializers(serializers.Serializer):
    pk = serializers.IntegerField()

class AlmaceSerializers(serializers.Serializer):
    almacen = OrdenSerializers(many=True)

#class AlmacenAgregarSerializer       