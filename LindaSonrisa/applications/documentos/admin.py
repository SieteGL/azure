from django.contrib import admin

from .models import (
    FichaTecnica,
    Procedimientos,
    Documento,
    EspecialistaProcedimiento
    )

admin.site.register(FichaTecnica)
admin.site.register(Procedimientos)
admin.site.register(EspecialistaProcedimiento)
admin.site.register(Documento)
