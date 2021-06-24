from django.contrib import admin

from .models import (Agenda,Reserva)

from applications.users.models import User

class AgendaAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'fecha',
        'especialista_agenda',
        #'display_tipo_usuario'
    )

    

    list_filter = ('fecha','especialista_agenda')

admin.site.register(Agenda, AgendaAdmin)
admin.site.register(Reserva)

