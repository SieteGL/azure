#
#from re import S
from django.utils import timezone
from datetime import datetime
#
from django.shortcuts import render
from rest_framework import serializers
# response
from rest_framework.response import Response
# Vistas
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    UpdateAPIView,
    DestroyAPIView
)
# serializadores
from .serializers import (
    CrearAgendaSerializer,
    AgendaSerializer,
    TomarHoraSerializer
)
# models
from .models import (
    Agenda,
    Reserva
)
# se debe pensar en que el especialista pondra a disposicion sus horas para que un cliente pueda tomar estas

#  dia datetime/ horas integerfield / especialista  USER/
#
# cliente dia y horas que toma del especialista
#

# PERTENECE AL ESPECIALISTA

#Muestra las horas disponibles por quien busca. LO VE ESPECIALISTA
class ListarAgenda(ListAPIView):
    serializer_class = AgendaSerializer
    def get_queryset(self):
        email = self.request.user.email
        return Agenda.objects.agenda_email(email)

#Especialista crea sus propias horas disponibles. LO VE ESPECIALISTA
class CrearAgenda(CreateAPIView):
    serializer_class = CrearAgendaSerializer
    def create(self, request, *args, **kwargs):
        serializer = CrearAgendaSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        list_hora = []
        hora = serializer.validated_data['hora']
        usuario = self.request.user.tipo_usuario
        if usuario == '1':
            for hr in hora:
                agenda = Agenda(
                    fecha=serializer.validated_data['fecha'],
                    hora=hr['hora'],
                    especialista_agenda=self.request.user
                )
                list_hora.append(agenda)             
            Agenda.objects.bulk_create(list_hora)
            if(len(list_hora) > 1):
                return Response({'SUCCESS': 'HORAS AGREGADAS CON EXITO'})
            else:
                return Response({'SUCCESS': 'HORA AGREGADA CON EXITO'})
        else:
            return Response({'ERROR': 'USTED NO ES UN ESPECIALISTA ...'})

#Eliminar una hora especifica pasar id de la hora que se desea eliminar. LO VE ESPECIALISTA
class EliminarHora(DestroyAPIView):
    serializer_class = AgendaSerializer
    queryset = Agenda.objects.all()  

###########
#El cliente podra visualizar las horas disponibles. Que el especialsita entrego Linea.45
class TomarHora(CreateAPIView):
    serializer_class = TomarHoraSerializer

    def create(self, request, *args, **kwargs):
        serializer = TomarHoraSerializer(data=request.data)
        serializer.is_valid(raise_exception=True) 
        agenda = serializer.validated_data['agenda']
        lista_agenda = []
        for agd in agenda:
            #recuperamos id de la agenda del especialista...(hora fecha)
            #crear signal para eliminar fecha de disponibilidad de la agenda
            hora = Agenda.objects.get(id=agd['pk'])
            #if hora != FileExistsError:
            rsv = Reserva(
                fecha = hora.fecha,
                hora = hora.hora,
                hora_cliente = self.request.user
            )
            lista_agenda.append(rsv)
        Reserva.objects.bulk_create(lista_agenda)    
        return Response({'SUCCESS','HORA TOMADA CON EXITO'})