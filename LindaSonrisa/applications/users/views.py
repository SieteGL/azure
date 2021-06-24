
# Django REST Framework
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
#
from rest_framework.generics import (
    ListAPIView,
)
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token

from rest_framework.permissions import  IsAuthenticated, IsAdminUser

# Serializers
from .serializers import (        
    ListarEspecialistas
)

# Models
from .models import User
# permissions
from .permissions import IsClienteUser

    
#listar especialistas
class ListarTipoUsuarios(ListAPIView):
    serializer_class = ListarEspecialistas
   
    #authentication_classes = (TokenAuthentication, )
    
    #permission_classes = [IsAuthenticated, ]#IsClienteUser]  

    def get_permissions(self):
        permission_classes = [IsAuthenticated, IsAdminUser, IsClienteUser]
        return [permission() for permission in permission_classes]     

    def get_queryset(self):
        usuario = self.request.user
        valor = self.kwargs['valor']  
        print(valor)
        #mostrar todos los usuarios 
        if valor == "9":
            return User.objects.all()
            #mostrar usuarios por tipo de usuario
        else:              
            return User.objects.listar_usuarios(valor)    


#listar Servicios por especialistas
