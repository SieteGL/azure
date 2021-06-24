
from django.db import models

class ConsultasManager(models.Manager):

    def documentos_por_user(self):
        return self.filter(
           cliente__tipo_usuario=3
        )

    def procedimientos_por_cliente(self, cliente):
        consulta = self.filter(
            cliente=cliente
        )
        return consulta
