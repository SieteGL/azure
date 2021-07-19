
# Django REST Framework
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
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
    CrearModelSerializer,
    #CustomTokenObtainPairSerializer
)

# Models
from .models import User
# permissions
from .permissions import IsClienteUser

    
#listar especialistas
class ListarTipoUsuarios(ListAPIView):

    serializer_class = ListarEspecialistas
    permission_classes = [IsAuthenticated, IsAdminUser]       
    
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
    permission_classes = [IsAuthenticated]

    def get_queryset(self):        
        return User.objects.traer_administradores()


#listar recepcionista
class ListarRecepcionista(ListAPIView):
    serializer_class = CrearModelSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):        
        return User.objects.traer_recepcionistas()


#listar especialistas
class ListarEspecialistas(ListAPIView):
    serializer_class = CrearModelSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):        
        return User.objects.traer_especialistas()


#listar clientes
class ListarClientes(ListAPIView):
    serializer_class = CrearModelSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):        
        return User.objects.traer_clientes()


#listar Servicios por especialistas
class ListarProveedores(ListAPIView):
    serializer_class = CrearModelSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):        
        return User.objects.traer_proveedores()

# class UpdateUser(UpdateAPIView):
#     serializer_class = CrearModelSerializer     
#     queryset = User.objects.all()

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    """Customizes JWT default Serializer to add more information about user"""
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # token['id'] = user.id        
        token['rut'] = user.rut
        token['name'] = user.nombre
        token['apellido'] = user.apellido
        token['email'] = user.email
        token['especialidades'] = user.especialidades
        token['is_superuser'] = user.is_superuser
        token['is_staff'] = user.is_staff
        token['is_active'] = user.is_active
        token['tipo_usuario'] = user.tipo_usuario
        token['is_esp'] = user.is_esp
        token['is_emp'] = user.is_emp
        token['is_cli'] = user.is_cli
        token['is_pro'] = user.is_pro
        return token   

class CustomTokenObtainPairView(TokenObtainPairView):
    # Replace the serializer with your custom
    serializer_class = CustomTokenObtainPairSerializer