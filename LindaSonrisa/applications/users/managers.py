from django.db import models

from django.contrib.auth.models import BaseUserManager

from django.db.models import Q, Sum, F, FloatField, ExpressionWrapper

class UserManager(BaseUserManager, models.Manager):

    #administrador de registro
    def _create_user(self, email, password, is_esp, is_emp, is_cli, is_pro ,tipo_usuario,is_staff, is_superuser, is_active, **extra_fields):
        user = self.model(            
            email=email,
            is_esp=is_esp,
            is_emp=is_emp,
            is_cli=is_cli,
            is_pro=is_pro,
            tipo_usuario=tipo_usuario,
            is_staff=is_staff,
            is_superuser=is_superuser,
            is_active=is_active,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self.db)
        return user

    
    #crear super usuario configuracion
    def create_superuser(self, email, password=None, **extra_fields):
        return self._create_user(email, password, False, False, False, False, '0',True, True, True, **extra_fields) 
    #crear especialista configuracion
    def create_especialista(self, email, password=None, **extra_fields):
        return self._create_user(email, password, True, False, False, False, '1', True, False, True, **extra_fields)   
    #crear recepcionista configurado
    def create_recepcionista(self, email, password=None, **extra_fields):
        return self._create_user(email, password, False, True, False, False, '2', True, False, True, **extra_fields) 
    #crear cliente configuracion
    def create_cliente(self, email, password=None, **extra_fields):
        return self._create_user(email, password, False, False, True, False, '3', False, False, True, **extra_fields)       
    #crear proveedor configuracion
    def create_proveedor(self, email, password=None, **extra_fields):
        return self._create_user(email, password, False, False, False, True, '4', False, False, True, **extra_fields)  
            

    def listar_especialistas(self):
        return self.filter(
           tipo_usuario=1 
        )
    #listando usuarios mediante un identificador que es el tipo de usuario
    def listar_usuarios(self, valor):
        return self.filter(
            tipo_usuario = valor
        )
                 
    def listar_especialidades(self, val):
        return self.filter(
            especialidades__icontains=val
        )

    def traer_proveedores(self):
        return self.filter(
            tipo_usuario=4,                      
        )            
      
         
        
