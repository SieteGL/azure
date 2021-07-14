 # django
from django.urls import include, path, re_path
# local
from . import views


app_name = "almacen_app"

urlpatterns = [
    path(
        'api/almacen/list',
        views.ListAlmacen.as_view(),
        name='almacen-lista',
    ),
    path(
        'api/cargar/almacen',
        views.CargarAlmacen.as_view(),
        name='almacen-crear',
    ),
]    