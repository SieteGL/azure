#
from re import S
from django.utils import timezone
from datetime import datetime

from django.shortcuts import render
#response
from rest_framework.response import Response
#Vistas
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    UpdateAPIView,
    DestroyAPIView
)
#serializadores
from .serializers import (
    ProcedimientoSerializer,
    FichaTecnicaSerializer,
    DocumentosSerializer,
    ProcesarDocumentos,
    ProcesarProcedimientos,
    ProcesarFichaTecnica,
    PaginationSerializer
    
)
from applications.users.permissions import IsEmployeeUser, IsClienteUser
from rest_framework.permissions import  IsAuthenticated, IsAdminUser
#models
from .models import (
    Documento,
    Procedimientos,
    FichaTecnica
)
#managers
from .managers import ConsultasManager


#Crear FichaTecnica del paciente
class CrearFichaTecnica(CreateAPIView):
    
    serializer_class = ProcesarFichaTecnica
    pagination_class = PaginationSerializer

    def create(self, request, *args, **kwargs):
        serializer = ProcesarFichaTecnica(data=request.data)
        serializer.is_valid(raise_exception=True)

        ficha = FichaTecnica.objects.create(
            enfermedad = serializer.validated_data['enfermedad'],
            alergia = serializer.validated_data['alergia'],
            enfermedades = serializer.validated_data['enfermedades'],
            alergias = serializer.validated_data['alergias'],
            cliente = self.request.user
        )
        ficha.save()

        return Response({'res':'Ficha tecnica del paciente creada'})


#############################################################

#Listar procedimientos por clientes
class ListarProcedimientos(ListAPIView):
    
    serializer_class = ProcedimientoSerializer
    pagination_class = PaginationSerializer

    def get_queryset(self):
        cliente = self.request.user
        return Procedimientos.objects.procedimientos_por_cliente(cliente)

#Agregar procedimiento a cliente
class CrearProcedimientos(CreateAPIView):

    serializer_class = ProcesarProcedimientos
    pagination_class = PaginationSerializer

    def create(self, request, *args, **kwargs):
        serializer = ProcesarProcedimientos(data=request.data)
        serializer.is_valid(raise_exception=True)

        procedimientos = Procedimientos.objects.create(
            fecha_procedimientos = timezone.now(),
            tipo_procedimiento = serializer.validated_data['tipo_procedimiento'],
            descripcion_procedimiento = serializer.validated_data['descripcion_procedimiento'],
            cliente = self.request.user
        )
        procedimientos.save()

        return Response({'res' : 'Procedimiento del cliente agregado'})

#actualizar procedimiento del paciente
class EditarProcedimientos(UpdateAPIView):

    serializer_class = ProcedimientoSerializer
    pagination_class = PaginationSerializer
    queryset = Procedimientos.objects.all()

#eliminar procedimiento por id del cliente
class EliminarProcedimientos(DestroyAPIView):
    serializer_class = ProcedimientoSerializer
    pagination_class = PaginationSerializer
    queryset = Procedimientos.objects.all()

####################################################

#dependiendo del tipo de documento se debe realizar la operacion para realizar
#descuento en la boleta final del usuario, se debe considerar los tipos de documentos 
#aceptados tomar el valor ingresado por el usuario, realizar filto de los 2 valores para 
#ver si es necesario realizar alguna revision extra de documentos.

#Listar Documentos x usuario
class ListDocumentsUser(ListAPIView):
    #queryset = User.objects.filter(is_active=True)
    serializer_class = DocumentosSerializer
    pagination_class = PaginationSerializer

    def get_queryset(self):               
        cliente = self.request.user
        #mostrando todos los datos ingresados por el usuario 
        return Documento.objects.documentos_por_user()

#Crear Documentos funcion usuarios
class CrearDocumentos(CreateAPIView):
    
    serializer_class = ProcesarDocumentos
    pagination_class = PaginationSerializer

    def create(self, request, *args, **kwargs):
        serializer = ProcesarDocumentos(data=request.data)
        serializer.is_valid(raise_exception=True)

        document = Documento.objects.create(
            documento = serializer.validated_data['documento'],
            valor = serializer.validated_data['valor'],
            imagen = serializer.validated_data['imagen'],
            cliente = self.request.user
        )
        document.save()
        return Response({'res' : 'documento agregado'})

class EditarDocumentos(UpdateAPIView):
    serializer_class = DocumentosSerializer
    permission_classes = [IsAuthenticated, IsClienteUser, IsAdminUser,]
    queryset = Documento.objects.all()

class DeleteDocumentos(DestroyAPIView):
    serializer_class = DocumentosSerializer
    permission_classes = [IsAuthenticated, IsClienteUser, IsAdminUser,]
    queryset = Documento.objects.all()
        
    