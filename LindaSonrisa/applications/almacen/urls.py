# django
from django.urls import include, path, re_path
# local
from . import views


app_name = "almacen_app"

urlpatterns = [
    path(
        'api/almacen/list',
        views.ListarAlmacen.as_view(),
        name='almacen-lista',
    ),
    path(
        'api/cargar/almacen',
        views.CargarAlmacenRecepcion.as_view(),
        name='almacen-crear',
    ),
]    