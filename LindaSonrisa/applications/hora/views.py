#
#from re import S
from typing import List
from django.utils import timezone
from datetime import datetime
#
from django.shortcuts import render
from rest_framework import serializers
# response
from rest_framework.response import Response
# Vistas
#Permisos
from rest_framework.permissions import  IsAuthenticated
from applications.users.permissions import IsEspecialistUser
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
    TomarHoraSerializer,
    HoraSerializer,
    UsuarioSerializer
)
# models
from .models import (
    Agenda,
    Reserva
)

from applications.users.models import User
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
    permission_classes = [IsAuthenticated, IsEspecialistUser ]   

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

# class EliminarHoraEspecialista(DestroyAPIView):
#     serializer_class = AgendaSerializer

#     def get_queryset(self):
#         valor = self.queryset.user
#         queryset = Agenda.objects.agenda_por_especialista(valor)
#         return queryset

###########
#El cliente podrá visualizar las horas disponibles. Que el especialsita entrego Linea.45
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
        #despues de agregar realizo la eliminacion de la hora del especialista.
        #recuperamos hora!
        agendita = Agenda.objects.recuperar_hora(hora.id)
        agendita.delete()
        return Response({'SUCCESS','HORA TOMADA CON EXITO'})

class ListHoraPaciente(ListAPIView):
    serializer_class = HoraSerializer
    def get_queryset(self):
        email = self.request.user.email
        return Reserva.objects.listar_horas(email)

class ListHoras(ListAPIView):
    serializer_class = HoraSerializer
    def get_queryset(self):        
        return Reserva.objects.all()

#lista informacion especialista full para ser mostrado en el front

#lista de especialistas muestra todos los especialistas del sistema
class ListarEspecialistas(ListAPIView):
    serializer_class = UsuarioSerializer

    def get_queryset(self):
        return User.objects.listar_especialistas()

#lista las especialidades y dependiendo del pk (id) muestra los doctores disponibles
class ListEspecialidades(ListAPIView):
    serializer_class = UsuarioSerializer
    def get_queryset(self):
        val = self.kwargs['pk']
        if val == '9':
            #ver si es correcto.
            return User.objects.listar_especialistas()
        else:            
            return User.objects.listar_especialidades(val)

#espera el pk del especialista para mostrar sus horas disponibles
class ListHorasEsp(ListAPIView):
    serializer_class = AgendaSerializer
    def get_queryset(self):
        val = self.kwargs['pk']
        return Agenda.objects.listar_agenda_especialista(val)

#listar usuarios donde su tipo de usuario sea tipo_usuario=1 y mostrar la lista 
 #de especialidades.
