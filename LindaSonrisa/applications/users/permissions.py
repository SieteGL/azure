from rest_framework.permissions import BasePermission

from .models import User

#client acceso
class IsClienteUser(BasePermission):
        
    def has_permission(self, request, view):

        try:            
            user = User.objects.get(email=request.user.email, is_cli=True)                                                   
        except User.DoesNotExist:
            return False
        return True

#especialista acceso
class IsEspecialistUser(BasePermission):

    def has_permission(self, request, view):

        try:
            user = User.objects.get(email=request.user.email, is_esp=True)
        except User.DoesNotExist:
            return False
        return True

#employee acceso
class IsEmployeeUser(BasePermission):

    def has_permission(self, request, view):

        try:
            user = User.objects.get(email=request.user.email, is_emp=True)
        except User.DoesNotExist:
            return False
        return True

#supplier acceso
class IsSupplierUser(BasePermission):

    def has_permission(self, request, view):

        try:
            user = User.objects.get(email=request.user.email, is_pro=True)
        except User.DoesNotExist:
            return False
        return True
