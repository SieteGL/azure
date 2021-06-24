from django.db import models

class BoletaManager(models.Manager):

    def boletas_por_usuario(self, usuario):
        consulta = self.filter(
            boleta__cliente = usuario            
        )
        return consulta



    