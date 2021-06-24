from rest_framework import permissions
from rest_framework.authtoken.models import Token
#from rest_framework.permissions import BasePermission

from .models import User

#client acceso
class IsClienteUser(permissions.BasePermission):

    def has_permission(self, request, view):

        try:
            user = User.objects.get(email=request.user)
        except User.DoesNotExist:
            return False
        return True

#admin acceso
"""
class IsAdminUser(permissions.BasePermission):
    
    def has_permission(self, request, view):

        try:
            user = User.objects.get(email=request.user, tipo_usuario=0)
        except User.DoesNotExist:
            return False
        return True
"""
#especialista acceso
class IsEspecialistUser(permissions.BasePermission):

    def has_permission(self, request, view):

        try:
            user = User.objects.get(email=request.user, tipo_usuario=1)
        except User.DoesNotExist:
            return False
        return True

#employee acceso
class IsEmployeeUser(permissions.BasePermission):

    def has_permission(self, request, view):

        try:
            user = User.objects.get(email=request.user, tipo_usuario=2)
        except User.DoesNotExist:
            return False
        return True

#supplier acceso
class IsSupplierUser(permissions.BasePermission):

    def has_permission(self, request, view):

        try:
            user = User.objects.get(email=request.user, tipo_usuario=4)
        except User.DoesNotExist:
            return False
        return True

