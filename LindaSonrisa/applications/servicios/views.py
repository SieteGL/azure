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
    ServiciosSerializer,
    ServiciosValidator,
    ListServiciosSerializer

)
# models
from .models import (
    Servicios,
    ServiciosList
)

class CrearListServicios(CreateAPIView):
    serializer_class = ListServiciosSerializer


# list de servicios disponibles con sus valores respectivos
class ListServicios(ListAPIView):
    serializer_class = ServiciosSerializer

    def get_queryset(self):
        user = self.request.user
        return Servicios.objects.all()


class CreateServicioView(CreateAPIView):
    #este muestra la informacion a pantalla 
    serializer_class = ServiciosSerializer
     


#class DescontarAlmacen(CreateAPIView):




#delete servicio y realizar liberacion de existencia en el almacen

##iterar servicios no listaservicios y cambiar orden de guardado revisar si surgen efectos