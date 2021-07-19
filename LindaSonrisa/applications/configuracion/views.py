#
#from re import S
from applications.users.permissions import IsEmployeeUser
from django.utils import timezone
from datetime import datetime

from django.shortcuts import render
from rest_framework import serializers
# response
from rest_framework.response import Response
#
from rest_framework import status
# Vistas
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    
)
# serializadores
from .serializers import (
    ConfigurarSerializer,
    EmpresaSerializer
)
# models
from .models import (
    Empresa
)
from rest_framework.permissions import  IsAuthenticated, IsAdminUser

class CrearConfiguracion(CreateAPIView):
    serializer_class = ConfigurarSerializer

    def create(self, request, *args, **kwargs):
        serializer = ConfigurarSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        empresa = Empresa.objects.create(
            nombre = serializer.validated_data['nombre'],
            rut = serializer.validated_data['rut'],
            pais = serializer.validated_data['pais'],
            codigo_area = serializer.validated_data['codigo_area'],
            contacto = serializer.validated_data['contacto'],
            año_fundacion = serializer.validated_data['año_fundacion'],
            representante = serializer.validated_data['representante'],
            region = serializer.validated_data['region'],
            comuna = serializer.validated_data['comuna'],
            calle = serializer.validated_data['calle'],
            numeracion = serializer.validated_data['numeracion'],
        )
        empresa.save()
        return Response(ConfigurarSerializer.data,status = status.HTTP_200_OK)

class ListEmpresa(ListAPIView):
    serializer_class = EmpresaSerializer

    def get_queryset(self):
        return Empresa.objects.all()