# django
from django.urls import include, path, re_path
# local
from . import views


app_name = "servicios_app"

urlpatterns = [
    path(
        'api/crear/lista/servicios',
        views.CrearListaServicios.as_view(),
        name='servicios-lista',
    ),
    path(
        'api/crear/servicios',
        views.CrearServicios.as_view(),
        name='servicios-lista',
    ),
    path(
        'api/servicios/lista',
        views.ListServicios.as_view(),
        name='servicios-lista',
    ),
    path(
        'api/list/servicios',
        views.ListServiciosList.as_view(),
        name='servicios-lista',
    ),
    # 
    # path(
    #     'api/agregar/servicio',
    #     views.CreateServicioView.as_view(),
    #     name='servicios-lista',
    # ),
]