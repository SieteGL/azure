
# Django REST Framework
from django.db.models import query
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
#
from rest_framework.generics import (
    ListAPIView,
    UpdateAPIView,
)
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token

from rest_framework.permissions import  IsAuthenticated, IsAdminUser

# Serializers
from .serializers import (        
    ListarEspecialistas,
    ListProveedores,
    CrearModelSerializer
)

# Models
from .models import User
# permissions
from .permissions import IsClienteUser

    
#listar especialistas
class ListarTipoUsuarios(ListAPIView):

    serializer_class = ListarEspecialistas
    permission_classes = [IsAuthenticated, IsAdminUser, ]       
    
    def get_queryset(self):
        # usuario = self.request.user
        valor = self.kwargs['valor']  
        print(valor)
        #mostrar todos los usuarios 
        if valor == "9":
            return User.objects.all()
            #mostrar usuarios por tipo de usuario
        else:              
            return User.objects.listar_usuarios(valor)    

#listar administradores
class ListarAdministradores(ListAPIView):
    serializer_class = CrearModelSerializer

    def get_queryset(self):        
        return User.objects.traer_administradores()


#listar recepcionista
class ListarRecepcionista(ListAPIView):
    serializer_class = CrearModelSerializer

    def get_queryset(self):        
        return User.objects.traer_recepcionistas()


#listar especialistas
class ListarEspecialistas(ListAPIView):
    serializer_class = CrearModelSerializer

    def get_queryset(self):        
        return User.objects.traer_especialistas()


#listar clientes
class ListarClientes(ListAPIView):
    serializer_class = CrearModelSerializer

    def get_queryset(self):        
        return User.objects.traer_clientes()


#listar Servicios por especialistas
class ListarProveedores(ListAPIView):
    serializer_class = CrearModelSerializer

    def get_queryset(self):        
        return User.objects.traer_proveedores()

# class UpdateUser(UpdateAPIView):
#     serializer_class = CrearModelSerializer     
#     queryset = User.objects.all()