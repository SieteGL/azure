from rest_framework import serializers, pagination
#
from .models import ServiciosList, Servicios
#
from rest_framework.validators import UniqueTogetherValidator, UniqueValidator
#
from rest_framework.response import Response


class ListServiciosSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiciosList
        fields = ('id','servicio',)


class ServiciosSerializer(serializers.ModelSerializer):
    servicios_lista = ListServiciosSerializer(many=True)
    
    class Meta:        
        model = Servicios        
        fields = ('id','name','valor_paquete','servicios_lista')
        depth = 1
    # def create(self, validated_data):
    #     servicios_lista_data = validated_data.pop('servicios_lista')
    #     servicios = Servicios.objects.create(**validated_data)
    #     servicios_lista_set_serializer = self.fields['servicios_lista']
    #     for each in servicios_lista_data:
    #         each['servicios'] = servicios
    #     servicios_list = servicios_lista_set_serializer.create(servicios_lista_data)
    #     return servicios
        
        
    
#agregar por servicios y se agregen en list crear una realcion en el serializer

class ServicioSerializers(serializers.Serializer):    
    servicio = serializers.CharField(validators=[
            UniqueValidator(queryset=ServiciosList.objects.all())])    



class PkSerializers(serializers.Serializer):
    pk = serializers.IntegerField()

class ServicesSerializers(serializers.Serializer):
    lista = PkSerializers(many=True)
    #servicio = serializers.CharField()
    name = serializers.CharField()
    valor = serializers.IntegerField()

class ListSerializers(serializers.Serializer):
    servicio_nombre = serializers.CharField()
    #servicio = ServicioSerializers(many=True)

