    #from LindaSonrisa.applications.recepcion.models import Detalles,Orden
from django.db import models
        
class RecepcionManager(models.Manager):

    def ordenes_nombres(self,name):
        consulta = self.filter(
            orden__name=name
        )
        return consulta     

    def orden_numero(self, nombre):
        consulta = self.filter(
            ordenes__name = nombre
        )#.order_by('-fecha') 
        return consulta    
    
    def nombres(self, name):
        return self.filter(
            orden__name = name
        )

    def estado_por_proveedor(self, user):
        consulta = self.filter(
            proveedores__tipo_usuario = user.tipo_usuario
        )
        return consulta

    def obtener_id(self):
        consulta = self.filter(
            proveedor__tipo_usuario=4,                                    
        )
        return consulta

    def traer_proveedores(self):
        return self.filter(
            proveedor__=4
        )        
    def ordenes_por_proveedor(self, user):
        return self.filter(
            proveedor_id=user
        )