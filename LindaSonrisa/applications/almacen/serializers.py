from django.db.models import fields
from rest_framework import serializers, pagination
#
from .models import Almacen, Disponible, Familia

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

class DisponiblesSerializers(serializers.ModelSerializer):

    class Meta:
        model=Disponible
        fields= '__all__'