#
from re import S
from django.utils import timezone
from datetime import datetime

from django.shortcuts import render
#response
from rest_framework.response import Response
from rest_framework import status
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
    PaginationSerializer,
    FichaUpdateSerializer
    
    
)
from applications.users.permissions import IsEmployeeUser, IsClienteUser
from applications.users.models import User
from rest_framework.permissions import  IsAuthenticated, IsAdminUser
#models
from .models import (
    Documento,
    Procedimientos,
    FichaTecnica,
    EspecialistaProcedimiento
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


#consumir el endpoint donde vienen todos los usuarios
class ListFichaTecnicaUsuario(ListAPIView):
    serializer_class = FichaTecnicaSerializer
    def get_queryset(self):
        valor = self.request.user
        return FichaTecnica.objects.ficha_usuario(valor)

class ListFichaTecnica(ListAPIView):
    def get_queryset(self):        
        return FichaTecnica.objects.all()

#############################################################
class ProcedimientoCrear(CreateAPIView):
    serializer_class = ProcesarProcedimientos

    def create(self, request, *args, **kwargs):
        serializer = ProcesarProcedimientos(data=request.data)
        serializer.is_valid(raise_exception=True)        

        procederes = EspecialistaProcedimiento.objects.create(
            fecha = timezone.now(),
            especialista = self.request.user
        )
        
        procedimientos_list = []

        procedimientos = serializer.validated_data['proceder']

        for proce in procedimientos:
            cliente = User.objects.get(id=proce['pk'])

            procedimniento = Procedimientos(
                tipo_procedimiento=serializer.validated_data['tipo_procedimiento'],
                descripcion_procedimiento=serializer.validated_data['descripcion_procedimiento'],
                cliente = cliente,
                Especialista_Procedimiento=procederes           
            )
            procedimientos_list.append(procedimniento)
        Procedimientos.objects.bulk_create(procedimientos_list)
        return Response({'SUCCESS':'PROCEDIMIENTO AGREGADO CON EXITO'})

#Listar procedimientos por clientes
class ListarProcedimientosCliente(ListAPIView):
    
    serializer_class = ProcedimientoSerializer
    pagination_class = PaginationSerializer

    def get_queryset(self):
        cliente = self.request.user
        return Procedimientos.objects.procedimientos_por_cliente(cliente)


class ListarProcedimientos(ListAPIView):
    serializer_class = ProcedimientoSerializer
    def get_queryset(self):        
        
        return Procedimientos.objects.all()

class EditarProcedimientos(UpdateAPIView):

    serializer_class = ProcedimientoSerializer
    pagination_class = PaginationSerializer
    queryset = Procedimientos.objects.all()

#eliminar procedimiento por id del cliente
class EliminarProcedimientos(DestroyAPIView):
    serializer_class = ProcedimientoSerializer
    pagination_class = PaginationSerializer
    queryset = Procedimientos.objects.all()

#Agregar procedimiento a cliente
"""class CrearProcedimientos(CreateAPIView):

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

        return Response({'res' : 'Procedimiento del cliente agregado'})"""

#actualizar procedimiento del paciente


####################################################

#dependiendo del tipo de documento se debe realizar la operacion para realizar
#descuento en la boleta final del usuario, se debe considerar los tipos de documentos 
#aceptados tomar el valor ingresado por el usuario, realizar filto de los 2 valores para 
#ver si es necesario realizar alguna revision extra de documentos.

#Listar Documentos x usuario
class ListDocumentsUser(ListAPIView):    
    serializer_class = DocumentosSerializer
    #pagination_class = PaginationSerializer

    def get_queryset(self):        
        return Documento.objects.all()

class ListDocumentsBoleta(ListAPIView):
    serializer_class = DocumentosSerializer

    def get_queryset(self):
        valor = self.kwargs['pk']
        return Documento.objects.usuario_boleta(valor)

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
    # permission_classes = [IsAuthenticated, IsClienteUser, IsAdminUser,]
    # queryset = Documento.objects.all()
    # def update(self, request, *args, **kwargs):
    #     partial = kwargs.pop('partial', False)
    #     instance = self.get_object()
    #     serializer = self.get_serializer(instance, data=request.data, partial=partial)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_update(serializer)
    #     return Response(serializer.data)

class DeleteDocumentos(DestroyAPIView):
    serializer_class = DocumentosSerializer
    permission_classes = [IsAuthenticated, IsClienteUser | IsAdminUser]
    queryset = Documento.objects.all()
        
class ListDocumentosCliente(ListAPIView):
    serializer_class = DocumentosSerializer

    def get_queryset(self):
        valor = self.request.user
        return Documento.objects.documentos_por_usuario(valor)

        
class FichaTecnicaUpdate(UpdateAPIView):
    serializer_class = FichaUpdateSerializer

    def get_queryset(self,pk):
        return self.get_serializer().Meta.model.objects.filter(id = pk).first()
    
    #muestra los datos a modificar
    def patch(self,request,pk=None):
        
        if self.get_queryset(pk):
            ficha_serializer = self.serializer_class(self.get_queryset(pk))
            return Response(ficha_serializer.data,status = status.HTTP_200_OK)
        return Response({'error','No existe ficha con estos datos'},status = status.HTTP_400_BAD_REQUEST)
    
    def put(self,request,pk=None):
        if self.get_queryset(pk):
            ficha_serializer = self.serializer_class(self.get_queryset(pk),data = request.data)
            if ficha_serializer.is_valid():
                ficha_serializer.save()
                return Response(ficha_serializer.data,status = status.HTTP_200_OK)
            return Response(ficha_serializer.data,errors = status.HTTP_400_BAD_REQUEST)