from django.contrib import admin

from .models import (
    FichaTecnica,
    Procedimientos,
    Documento
    )

admin.site.register(FichaTecnica)
admin.site.register(Procedimientos)
admin.site.register(Documento)