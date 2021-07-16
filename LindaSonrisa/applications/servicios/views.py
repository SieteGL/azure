#
#from re import S
from applications.users.permissions import IsEmployeeUser
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
    ServicesSerializers,
    ListSerializers,
    ServiciosSerializer,
    # ServiciosValidator,
    ListServiciosSerializer

)
# models
from .models import (
    Servicios,
    ServiciosList
)
from rest_framework.permissions import  IsAuthenticated, IsAdminUser

class CrearListaServicios(CreateAPIView):
    serializer_class = ListSerializers

    def create(self, request, *args, **kwargs):
        serializer = ListSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)

        ServiciosList.objects.create(
            servicio = serializer.validated_data['servicio_nombre']
        )        
        return Response({'SUCCESS':'AGREGADO CON EXITO'})               

                     
class CrearServicios(CreateAPIView):
    serializer_class = ServiciosSerializer

    def create(self, request, *args, **kwargs):
        serializer = ServiciosSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        servicios_obj = Servicios.objects.create(
            name=serializer.validated_data['name'],
            valor_paquete=serializer.validated_data['valor_paquete']
        )
        servicios_obj.save()

        for list in serializer.validated_data['servicios_lista']:
            list_obj = ServiciosList.objects.get(id=list['servicio'])
            servicios_obj.servicios_lista.add(list_obj)
        serializer = ServiciosSerializer(servicios_obj)    

        return Response(serializer.data)            

        
class ListServicios(ListAPIView):
    serializer_class = ServiciosSerializer
    permission_classes = [IsAuthenticated, IsEmployeeUser|IsAdminUser ]   

    def get_queryset(self):
        user = self.request.user
        return Servicios.objects.all()

class ListServiciosList(ListAPIView):
    serializer_class =ListServiciosSerializer
    def get_queryset(self):
        return ServiciosList.objects.all()

class EliminarListServicios(DestroyAPIView):
    serializer_class = ListServiciosSerializer  
    
    def get_queryset(self):
        queryset = ServiciosList.objects.all()                 
        return queryset

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()            
        self.perform_destroy(instance)  
        return Response({'SUCCESS':'ELIMINADO CON EXITO'})

class EliminarServicios(DestroyAPIView):
    serializer_class = ServiciosSerializer  
    
    def get_queryset(self):
        queryset = Servicios.objects.all()                 
        return queryset

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()            
        self.perform_destroy(instance)  
        return Response({'SUCCESS':'ELIMINADO CON EXITO'})

#falta ver que paso con el edit
class UpdateServicios(UpdateAPIView):
    serializer_class = ServiciosSerializer 
    queryset = Servicios.objects.all() 
    
