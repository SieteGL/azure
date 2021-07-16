from rest_framework import serializers, pagination
#
from .models import Almacen, Familia

class AlmacenSerializers(serializers.ModelSerializer):
 
    class Meta:
        model = Almacen
        fields = '__all__'

class OrdenSerializers(serializers.Serializer):
    pk = serializers.IntegerField()

class AlmaceSerializers(serializers.Serializer):
    almacen = OrdenSerializers(many=True)     

class PruebaSerializers(serializers.Serializer):
    stock = serializers.IntegerField()