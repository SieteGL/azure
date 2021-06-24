#
#from re import S
from django.utils import timezone
from datetime import datetime

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
    AgendaSerializer

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

class ListarAgenda(ListAPIView):

    serializer_class = AgendaSerializer

    def get_queryset(self):
        email = self.request.user.email
        return Agenda.objects.agenda_email(email)


class CrearAgenda(CreateAPIView):

    serializer_class = CrearAgendaSerializer

    def create(self, request, *args, **kwargs):
        serializer = CrearAgendaSerializer(data=request.data)
        serializer.is_valid(raise_exception=True) 
        list_hora = []
        hora = serializer.validated_data['hora']
        for hr in hora:
            agenda = Agenda(
                fecha=serializer.validated_data['fecha'],
                hora=hr['hora'],
                especialista_agenda=self.request.user
            )
            list_hora.append(agenda)
        Agenda.objects.bulk_create(list_hora)
        return Response({'RES': 'OK'})

        
