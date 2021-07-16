
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

    def ficha_usuario(self, valor):
        return self.filter(
            cliente_id=valor
        )        

    def documentos_por_usuario(self, valor):
        return self.filter(
            cliente=valor
        )
    
    
    # def ficha_tecnica_usuario(self, user):
    #     return self.filter(
    #         cliente=user
    #     )        
