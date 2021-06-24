from django.db import models

class ServiciosManager(models.Manager):

    def servicios_por_especialista(self):
        consulta = self.filter(
            servicios=2
        )

    def recuperar_lista(self, service):
        consulta = self.filter(
            servicios_listar=service
        )    
        return consulta 