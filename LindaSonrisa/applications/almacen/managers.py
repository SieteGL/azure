from datetime import timedelta
#
from django.db import models
from django.utils import timezone
from django.db.models import Q, F

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

    def filtrar_almacen(self, **filtros):        
        """if not filtros['fecha']:
            filtros['fecha'] = '2021-01-01'

        if not filtros['fecha_vencimiento']:
            filtros['fecha_vencimiento'] = timezone.now().date() + timedelta(1080)    


        consulta = self.filter(
            fecha_vencimiento__range=(filtros['fecha'], filtros['fecha_vencimiento'])
        )
        
        consulta = self.filter(
            codigo__icontains = filtros['codigo']
        )"""

        return self.filter(
            codigo__icontains=filtros['code'],
            stock__icontains=filtros['stock']            
        )

    
