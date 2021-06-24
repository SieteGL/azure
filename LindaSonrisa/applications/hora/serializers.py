from rest_framework import serializers, pagination
#
from .models import Agenda, Reserva
#
from rest_framework.validators import UniqueValidator

#crear lista de horas para la misma fecha y agregar una sola vez...

class AgendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agenda
        fields = ('id','fecha','hora','especialista_agenda')

class AgendaHoraSerializer(serializers.Serializer):             
    hora = serializers.CharField()
class CrearAgendaSerializer(serializers.Serializer): 
    fecha = serializers.DateField()         
    hora = AgendaHoraSerializer(many=True)