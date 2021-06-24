# django
from django.urls import include, path, re_path
# local
from . import views

app_name = "recepcion_app"

urlpatterns = [
    path(
        'api/listar/orden/<nombre>',
        views.ListOrdenPedidos.as_view(),
        name='listar-orden'
    ),
    path(
        'api/crear/orden',
        views.CrearOrdenPedidos.as_view(),
        name='crear-orden-productos',
    ),
    path(
        'api/actualizar/estado',
        views.UpdateEstado.as_view(),
        name='actualizar-orden-productos',
    ),
    path(
        'api/crear/recepcion',
        views.RevisarRecepcionAlmacen.as_view(),
        name='actualizar-recepcion-almacen',
    )
    
]