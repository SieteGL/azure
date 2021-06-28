from django.db import models

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from .managers import UserManager

from applications.servicios.models import Servicios

class User(AbstractBaseUser, PermissionsMixin):

    #TIPOS DE USUARIOS
    ADMINISTRADOR = '0'
    ESPECIALISTA = '1'
    RECEPCIONISTA = '2'
    CLIENTE = '3'
    PROVEEDOR = '4'
    #GENEROS
    HOMBRE = 'M'
    MUJER = 'F'
    OTRO = 'O'
    #ESPECIALIDAD
    #ODONTOLOGO GENERAL
    ODONTOLOGO = '0'
    #FRENILLOS | ORTODONCIA
    ORTODONCISTA = '1'
    #RADIOGRAFIAS | BITE WING 
    RADIOLOGO = '2'
    #PROTESIS
    PROSTODONCISTA = '3'


    USUARIO_CHOICES = [
        (ADMINISTRADOR, 'Administrador'),
        (ESPECIALISTA, 'Especialista'),
        (RECEPCIONISTA, 'Recepcionista'),
        (CLIENTE, 'Cliente'),
        (PROVEEDOR, 'Proveedor'),        
    ]

    GENERO_CHOICES = [
        (HOMBRE, 'Masculino'),
        (MUJER, 'Femenino'),
        (OTRO, 'Otros'),
    ]

    ESPECIALIDAD_CHOICES = [
        (ODONTOLOGO,'Odontologo General'),
        (ORTODONCISTA,'Ortodoncista'),
        (RADIOLOGO,'Radiologo'),
        (PROSTODONCISTA,'Prostodoncista'),
    ]

    rut = models.CharField(
        max_length=13,
        blank=True
    )

    email = models.EmailField(
        unique=True
    )

    nombre = models.CharField(
        'nombre',
        max_length=30,
        blank=True
    )

    apellido = models.CharField(
        'apellidos',
        max_length=30,
        blank=True
    )

    tipo_usuario = models.CharField(
        max_length=1,
        choices=USUARIO_CHOICES,
        blank=True
    )

    sexo = models.CharField(
        max_length=1,
        choices=GENERO_CHOICES,
        blank=True
    )

    especialidades = models.CharField(
        max_length=1,
        choices=ESPECIALIDAD_CHOICES,
        blank=True
    )

    fecha_nacimiento = models.DateField(
        'Fecha de nacimiento',
        blank=True,
        null=True
        #modificar ejemplo practico
    )
    #
    is_staff = models.BooleanField(
        default=False
    )
    #
    is_active = models.BooleanField(
        default=False
    )

    region = models.CharField(
        max_length=25,
        blank=True
    )

    ciudad = models.CharField(
        max_length=30,
        blank=True
    )

    comuna = models.CharField(
        max_length=25,
        blank=True
    )

    direccion = models.CharField(
        max_length=50,
        blank=True
    )

    numero = models.CharField(
        'Número de casa',
        max_length=6,
        blank=True
    )

    contacto = models.PositiveIntegerField(
        'Numero de contacto',
        blank=True
    )

    is_esp = models.BooleanField(default=False)
    is_emp = models.BooleanField(default=False)
    is_cli = models.BooleanField(default=False)
    is_pro = models.BooleanField(default=False)

    servicios = models.ManyToManyField(Servicios,blank=True)

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['rut','nombre','apellido']

    objects = UserManager()


    #devolvemos email interno del usuario
    def display_email(self):
        return ''.join([email for email in self.email[:100]])

    display_email.short_description = 'email'
    #devolvemos el tipo de usuario
    def display_tipo_usuario(self):      
                                  
        return ''.join([tipo_usuario for tipo_usuario in self.tipo_usuario[:1]])

    display_tipo_usuario.short_description = 'tipo usuario'

   

    
    class Meta:
        verbose_name = "Usuarios registrado"    

    def __str__(self):
        return str(self.display_email())+' - '+str(self.display_tipo_usuario())