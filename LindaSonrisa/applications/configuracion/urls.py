# django
from django.urls import include, path, re_path
# local
from . import views


app_name = "documentos_app"

urlpatterns = [
    path(
        'api/crear/empresa',
        views.CrearConfiguracion.as_view(),
        name='crear-empresa',
    ),
    path(
        'api/listar/empresa',
        views.ListEmpresa.as_view(),
        name='crear-empresa',
    ),
]