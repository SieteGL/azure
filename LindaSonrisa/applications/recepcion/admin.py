from django.contrib import admin

from .models import (Orden,Recepcion,Detalles,Estado)

admin.site.register(Orden)
admin.site.register(Recepcion)
admin.site.register(Detalles)
admin.site.register(Estado)