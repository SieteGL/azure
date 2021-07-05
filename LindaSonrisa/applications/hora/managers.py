from django.db import models
from applications.users.models import User
        
class AgendaManager(models.Manager):

    def ordenes_nombres(self,fecha):
        consulta = self.filter(
            agenda__fecha=fecha
        )
        return consulta    

    def obtener_especialistas(self):
        consulta = self.filter(
            user__tipo_usuario=1
        )
        #obtener horas por especialista mediante email
    def agenda_email(self, email):
        return self.filter(
            especialista_agenda_id__email=email
        )
    def listar_horas(self, email):
        return self.filter(
            hora_cliente_id__email=email
        )