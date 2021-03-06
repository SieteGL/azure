
# Django REST Framework
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
#
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy, reverse

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
    UserModelSerializer,
    UserLoginSerializer,
    AdminSignUpSerializer,
    EspecialistaSignUpSerializer,
    RecepSignUpSerializer,
    ClienteSignUpSerializer,
    ProveedorSignUpSerializer,
    #
    CrearModelSerializer,
    #Listar especialista
    ListarEspecialistas
)

# Models
from .models import User

#se dejo de usar porque se implemento JWT para validacion mediante Token
class UserViewSet(viewsets.GenericViewSet):

    queryset = User.objects.filter(is_active=True)
    serializer_class = UserModelSerializer

    # Detail define si es una petición de detalle o no, en methods añadimos el método permitido, en nuestro caso solo vamos a permitir post
    @action(detail=False, methods=['post'])
    def login(self, request):
        """User sign in."""
        
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)                        
        user, token = serializer.save()        
        data = {            
            'user': UserModelSerializer(user).data,
            'access_token': token
        }
        #realizo la redireccion luego del login 
        return Response(data, status=status.HTTP_201_CREATED)
        #return HttpResponseRedirect(reverse('documentos_app:crear-documento-cliente'))

class CrearViewSet(viewsets.GenericViewSet):

    queryset = User.objects.filter(is_active=True)
    serializer_class = CrearModelSerializer
    
    #def get_permissions(self):
    permission_classes = [IsAuthenticated, IsAdminUser]
        #return [permission() for permission in permission_classes]  

    #ADMINISTRADOR
    @action(detail=False, methods=['post'])
    def admin(self, request):
        """User sign up."""
        serializer = AdminSignUpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        #        
        token = Token.objects.create(user=user)
        #
        data = CrearModelSerializer(user).data
        return Response(data, status=status.HTTP_201_CREATED)

    #ESPECIALISTA 
    @action(detail=False, methods=['post'])
    def espe(self, request):
        """User sign up."""
        serializer = EspecialistaSignUpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        if serializer.validated_data['region'] != None:
            user = serializer.save()
        #token = Token.objects.create(user=user)
            data = CrearModelSerializer(user).data
            return Response(data, status=status.HTTP_201_CREATED)
        else:
            return Response({'ERROR':'INGRESE UNA REGION VALIDA'})           
        #return HttpResponseRedirect(reverse(''))

    #RECEPCIONISTA
    @action(detail=False, methods=['post'])
    def recep(self, request):
        """User sign up."""
        serializer = RecepSignUpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        #token = Token.objects.create(user=user)
        data = CrearModelSerializer(user).data
        return Response(data, status=status.HTTP_201_CREATED)

    #PROVEEDOR
    @action(detail=False, methods=['post'])
    def pro(self, request):
        """User sign up."""
        serializer = ProveedorSignUpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        #token = Token.objects.create(user=user)
        data = CrearModelSerializer(user).data
        return Response(data, status=status.HTTP_201_CREATED)
    

class CrearClienteViewSet(viewsets.GenericViewSet):
    serializer_class = CrearModelSerializer
    
    #CLIENTE
    @action(detail=False, methods=['post'])
    def cli(self, request):
        """User sign up."""
        serializer = ClienteSignUpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        #token = Token.objects.create(user=user)
        data = CrearModelSerializer(user).data
        return Response(data, status=status.HTTP_201_CREATED)

# class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
#     """Customizes JWT default Serializer to add more information about user"""
#     @classmethod
#     def get_token(cls, user):
#         token = super().get_token(user)
#         token['id'] = user.id
#         token['name'] = user.name
#         token['email'] = user.email
#         token['is_superuser'] = user.is_superuser
#         token['is_staff'] = user.is_staff
#         token['tipo_usuario'] = user.tipo_usuario
#         token['is_active'] = user.is_active

#         return token   

# class CustomTokenObtainPairView(TokenObtainPairView):
#     # Replace the serializer with your custom
#     serializer_class = CustomTokenObtainPairSerializer        