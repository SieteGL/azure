from applications.users.models import User
from rest_framework import serializers, pagination
#
from .models import Agenda, Reserva
#
from rest_framework.validators import UniqueValidator
#from applications.users.models import User

#crear lista de horas para la misma fecha y agregar una sola vez...

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'nombre',
            'apellido',
            'especialidades'
            )


class AgendaSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Agenda
        fields = (
            'id',
            'fecha',
            'hora',
            'especialista_agenda',
        )

class AgendaHoraSerializer(serializers.Serializer):             
    hora = serializers.CharField()
class CrearAgendaSerializer(serializers.Serializer): 
    fecha = serializers.DateField()         
    hora = AgendaHoraSerializer(many=True)

class PkSerializer(serializers.Serializer):
    pk = serializers.IntegerField()

class TomarHoraSerializer(serializers.Serializer):
    agenda = PkSerializer(many=True)

class HoraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        fields = (
            'id',
            'fecha',
            'hora',
            'hora_cliente'
        )