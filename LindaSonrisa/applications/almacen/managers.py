from django.db import models

class AlmacenManager(models.Manager):

    def almacen_por_empleado(self, usuario):
        return self.filter(
            empleado__tipo_usuario=usuario.tipo_usuario,
            #empleado__email=usuario.email
        )

    def almacen_por_email(self, usuario):
        return self.filter(
            empleado__email=usuario.email
        )    

    
