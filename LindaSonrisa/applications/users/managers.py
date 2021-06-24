from django.db import models

from django.contrib.auth.models import BaseUserManager

from django.db.models import Q, Sum, F, FloatField, ExpressionWrapper

class UserManager(BaseUserManager, models.Manager):

    #administrador de registro
    def _create_user(self, email, password, tipo_usuario,is_staff, is_superuser, is_active, **extra_fields):
        user = self.model(            
            email=email,
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
        return self._create_user(email, password, '0',True, True, True, **extra_fields) 
    #crear especialista configuracion
    def create_especialista(self, email, password=None, **extra_fields):
        return self._create_user(email, password, '1', True, False, True, **extra_fields)   
    #crear recepcionista configurado
    def create_recepcionista(self, email, password=None, **extra_fields):
        return self._create_user(email, password, '2', True, False, True, **extra_fields) 
    #crear cliente configuracion
    def create_cliente(self, email, password=None, **extra_fields):
        return self._create_user(email, password, '3', False, False, True, **extra_fields)       
    #crear proveedor configuracion
    def create_proveedor(self, email, password=None, **extra_fields):
        return self._create_user(email, password, '4', False, False, True, **extra_fields)  
            

    def listar_especialistas(self):
        return self.filter(
           tipo_usuario=1
        )
    #listando usuarios mediante un identificador que es el tipo de usuario
    def listar_usuarios(self, valor):
        return self.filter(
            tipo_usuario = valor
        )
                 
        
       
      
         
        
