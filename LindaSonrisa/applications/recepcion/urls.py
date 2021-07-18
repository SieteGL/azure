# django
from django.urls import include, path, re_path
# local
from . import views

app_name = "recepcion_app"

urlpatterns = [
    # path(
    #     'api/listar/orden/<nombre>',
    #     views.ListOrdenPedidos.as_view(),
    #     name='listar-orden'
    # ),
    # # path(
    # #     'api/crear/orden',
    # #     views.CrearOrdenPedidos.as_view(),
    # #     name='crear-orden-productos',
    # # ),
    # path(
    #     'api/actualizar/estado',
    #     views.UpdateEstado.as_view(),
    #     name='actualizar-orden-productos',
    # ),
    # path(
    #     'api/crear/recepcion',
    #     views.RevisarRecepcionAlmacen.as_view(),
    #     name='actualizar-recepcion-almacen',
    # ),


    ##REALIZANDO PRUEBAS

    path(
        'api/pedido/p',
        views.CrearPedido.as_view(),
        name='crear',
    ),
    path(
        'api/listar/recepcion',
        views.ListRecepcion.as_view(),
        name='listar'
    ),
    path(
        'api/crear/recepcion',
        views.CrearRecepcion.as_view(),
        name='crear-recepcion'
    ),
    path(
        'api/listar/ordenes/proveedor',
        views.ListOrdenesProveedores.as_view(),
        name='crear-recepcion'
    ),
    path(
        'api/crear/actualizacion/estados',
        views.ActualizarEstado.as_view(),
        name='Actualizar-estado'
    ),
    path(
        'api/listar/ordenes',
        views.ListDetalles.as_view(),
        name='Actualizar-estado'
    ),
    path(
        'api/listar/no/agregados',
        views.ListAgregados.as_view(),
        name='Actualizar-estado'
    ),
    
]