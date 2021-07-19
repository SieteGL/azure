"""Users serializers."""

# Django
from django.contrib.auth import password_validation, authenticate
#
from django.core.validators import RegexValidator, FileExtensionValidator
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
# Django REST Framework
from rest_framework import serializers, pagination
from rest_framework.authtoken.models import Token
#
from rest_framework.validators import UniqueValidator
# Models
from .models import User
#
from applications.servicios.models import Servicios


class ListProveedores(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','rut','email','id')

class PaginationSerializer(pagination.PageNumberPagination):
    page_size = 5
    max_page_size = 50

#crear data para json para cada tipo de usuario y asignar al view de cada uno de los tipos de usuarios
class UserModelSerializer(serializers.ModelSerializer):
    #last_login = serializers.DateField()
    class Meta:
        model = User
        fields =  (
            'id',
            'email',
            'password',            
        )

class CrearModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        #mandar informacion necesarias
        fields = ('__all__')        
        

class UserLoginSerializer(serializers.Serializer):

    # Campos que vamos a requerir
    

    email = serializers.EmailField()
    password = serializers.CharField(min_length=5, max_length=64)

    # Primero validamos los datos
    def validate(self, data):
        

        # authenticate recibe las credenciales, si son válidas devuelve el objeto del usuario
        user = authenticate(username=data['email'], password=data['password'])
        if not user:
            raise serializers.ValidationError('Las credenciales no son válidas')

        # Guardamos el usuario en el contexto para posteriormente en create recuperar el token
        self.context['user'] = user
        return data

    def create(self, data):
        """Generar o recuperar token."""
        token, created = Token.objects.get_or_create(user=self.context['user'])
        return self.context['user'], token.key


#SERIALIZAMOS LOS DATOS DE SERVICIOS POR ESPECIALISTA ---
class ListarServiciosPorEspecialista(serializers.ModelSerializer):
    class Meta:
        model = Servicios
        fields = (
            'id',
            'name',
        )

class ListarEspecialistas(serializers.ModelSerializer):
    # servicios = ListarServiciosPorEspecialista(many=True)

    class Meta:
        model = User
        fields = [
            'id',
            'email',
            'rut',
            'nombre',
            'apellido',
            'sexo',
            'fecha_nacimiento',
            'region',
            'ciudad',
            'comuna',
            'direccion',
            'numero',
            'especialidades',
            # 'servicios',                        
        ]
#---


#Validar datos admin.
class AdminSignUpSerializer(serializers.Serializer):

    #no pido valores a validar y guardar. revisar por si es necesario realizar algun cambio
    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    """
    username = serializers.CharField(
        min_length=4,
        max_length=20,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    """
    
    rut = serializers.CharField(max_length=13, required=False)

    region = serializers.CharField(max_length=250, required=False)

    direccion = serializers.CharField(max_length=250, required=False)

    """
    phone_regex = RegexValidator(
        regex=r'\+?1?\d{9,15}$',
        message="Debes introducir un número con el siguiente formato: +999999999. El límite son de 15 dígitos."
    )
    phone = serializers.CharField(validators=[phone_regex], required=False)"""

    password = serializers.CharField(min_length=8, max_length=64)
    password_confirmation = serializers.CharField(min_length=8, max_length=64)

    nombre = serializers.CharField(min_length=2, max_length=50)
    apellido = serializers.CharField(min_length=2, max_length=100)       

    
    def validate(self, data):
        passwd = data['password']
        passwd_conf = data['password_confirmation']
        if passwd != passwd_conf:
            raise serializers.ValidationError("Las contraseñas no coinciden")
        password_validation.validate_password(passwd)
        return data        
           

    def create(self, data):
        data.pop('password_confirmation')
        user = User.objects.create_superuser(**data)
        return user 
#validad datos especialista
class EspecialistaSignUpSerializer(serializers.Serializer):
    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    rut = serializers.CharField(max_length=13, required=True)

    password = serializers.CharField(min_length=8, max_length=64)
    password_confirmation = serializers.CharField(min_length=8, max_length=64)

    nombre = serializers.CharField(min_length=2, max_length=50)
            
    apellido = serializers.CharField(min_length=2, max_length=100)         
            
    sexo = serializers.CharField(min_length=1, max_length=1)       
            
    fecha_nacimiento =serializers.DateField(input_formats=['%d-%m-%Y'])        

    region = serializers.CharField(max_length=50, required=True)

    ciudad = serializers.CharField(max_length=50, required=True)

    comuna = serializers.CharField(max_length=50, required=True)

    direccion = serializers.CharField(max_length=50, required=True)

    especialidades = serializers.CharField(max_length=50, required=True)

    numero = serializers.IntegerField(min_value=1, max_value=10000)

    contacto = serializers.IntegerField()

    

    def validate(self, data):
        passwd = data['password']
        passwd_conf = data['password_confirmation']
        if passwd != passwd_conf:
            raise serializers.ValidationError("Las contraseñas no coinciden")
        password_validation.validate_password(passwd)
        return data   

    def create(self, data):
        data.pop('password_confirmation')
        user = User.objects.create_especialista(**data)
        return user
#validar datos recepcionista
class RecepSignUpSerializer(serializers.Serializer):
    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    rut = serializers.CharField(max_length=13, required=True)

    password = serializers.CharField(min_length=8, max_length=64)
    password_confirmation = serializers.CharField(min_length=8, max_length=64)

    nombre = serializers.CharField(min_length=2, max_length=50)
            
    apellido = serializers.CharField(min_length=2, max_length=100)         
            
    sexo = serializers.CharField(min_length=1, max_length=1)       
            
    fecha_nacimiento =serializers.DateField(input_formats=['%d-%m-%Y'])        

    region = serializers.CharField(max_length=50, required=True)

    ciudad = serializers.CharField(max_length=50, required=True)

    comuna = serializers.CharField(max_length=50, required=True)

    direccion = serializers.CharField(max_length=50, required=True)

    numero = serializers.IntegerField(min_value=1, max_value=10000)

    contacto = serializers.IntegerField()

    def validate(self, data):
        passwd = data['password']
        passwd_conf = data['password_confirmation']
        if passwd != passwd_conf:
            raise serializers.ValidationError("Las contraseñas no coinciden")
        password_validation.validate_password(passwd)
        return data   

    def create(self, data):
        data.pop('password_confirmation')
        user = User.objects.create_recepcionista(**data)
        return user 
#validar datos cliente
class ClienteSignUpSerializer(serializers.Serializer):

    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    rut = serializers.CharField(max_length=13, required=True)

    password = serializers.CharField(min_length=8, max_length=64)
    password_confirmation = serializers.CharField(min_length=8, max_length=64)

    nombre = serializers.CharField(min_length=2, max_length=50)
            
    apellido = serializers.CharField(min_length=2, max_length=100)         
            
    sexo = serializers.CharField(min_length=1, max_length=1)       
            
    fecha_nacimiento =serializers.DateField(input_formats=['%d-%m-%Y'])        

    region = serializers.CharField(max_length=50, required=True)

    ciudad = serializers.CharField(max_length=50, required=True)

    comuna = serializers.CharField(max_length=50, required=True)

    direccion = serializers.CharField(max_length=50, required=True)

    numero = serializers.IntegerField(min_value=1, max_value=10000)

    contacto = serializers.IntegerField()

    def validate(self, data):
        passwd = data['password']
        passwd_conf = data['password_confirmation']
        if passwd != passwd_conf:
            raise serializers.ValidationError("Las contraseñas no coinciden")
        password_validation.validate_password(passwd)
        return data   

    def create(self, data):
        data.pop('password_confirmation')
        user = User.objects.create_cliente(**data)
        return user      
#validar datos proveedor
class ProveedorSignUpSerializer(serializers.Serializer):
    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    rut = serializers.CharField(max_length=13, required=True)

    password = serializers.CharField(min_length=8, max_length=64)
    password_confirmation = serializers.CharField(min_length=8, max_length=64)

    nombre = serializers.CharField(min_length=2, max_length=50)
            
    apellido = serializers.CharField(min_length=2, max_length=100)         
            
    sexo = serializers.CharField(min_length=1, max_length=1)       
            
    fecha_nacimiento =serializers.DateField(input_formats=['%d-%m-%Y'])        

    region = serializers.CharField(max_length=50, required=True)

    ciudad = serializers.CharField(max_length=50, required=True)

    comuna = serializers.CharField(max_length=50, required=True)

    direccion = serializers.CharField(max_length=50, required=True)

    numero = serializers.IntegerField(min_value=1, max_value=10000)

    contacto = serializers.IntegerField()

    def validate(self, data):
        passwd = data['password']
        passwd_conf = data['password_confirmation']
        if passwd != passwd_conf:
            raise serializers.ValidationError("Las contraseñas no coinciden")
        password_validation.validate_password(passwd)
        return data   

    def create(self, data):
        data.pop('password_confirmation')
        user = User.objects.create_proveedor(**data)
        return user            


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