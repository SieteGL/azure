from rest_framework import serializers, pagination
#
from .models import ServiciosList, Servicios
#
from rest_framework.validators import UniqueTogetherValidator, UniqueValidator


class ListServiciosSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiciosList
        fields = ('__all__')


class ServiciosSerializer(serializers.ModelSerializer):
    #servicios_listar = ListServiciosSerializer( many=True)
    
    class Meta:        
        model = Servicios        
        fields = (
            'id',
            'servicios_lista',
            'name',
            'valor_paquete',
            #'servicios_listar'
        )    
        validators = [
            UniqueTogetherValidator(
                queryset=Servicios.objects.all(),
                fields=['name',]
            )
        ]
    


#agregar por servicios y se agregen en list crear una realcion en el serializer

class Servicio(serializers.Serializer):    
    servicio = serializers.CharField(validators=[UniqueValidator(queryset=ServiciosList.objects.all())])    

class ServiciosValidator(serializers.Serializer):
    #para ListaServicios
    servicio = Servicio(many=True)
    #servicio = ServiciosSerializer(many=True)  
    #Servicios paquetes     
    #listita = ServiciosSerializer()
    #name = ServiciosSerializer()
    #valor_paquete = ServiciosSerializer()


       