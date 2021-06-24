# django
from django.urls import include, path, re_path
# local
from . import views


app_name = "documentos_app"

urlpatterns = [
    path(
        'api/agregar/ficha',
        views.CrearFichaTecnica.as_view(),
        name='crear-ficha-cliente',
    ),
    path(
        'api/listar/procedimiento',
        views.ListarProcedimientos.as_view(),
        name='listar-procedimiento-cliente',
    ),
    path(
        'api/agregar/procedimiento',
        views.CrearProcedimientos.as_view(),
        name='crear-procedimiento-cliente',
    ),
    path(
        'api/editar/Procedimiento/<pk>',
        views.EditarProcedimientos.as_view(),
        name='editar-procedimiento-cliente',
    ),
    path(
        'api/eliminar/Procedimiento/<pk>',
        views.EliminarProcedimientos.as_view(),
        name='eliminar-procedimiento-cliente',
    ),
    path(
        'api/documentos/usuario',
        views.ListDocumentsUser.as_view(),
        name='documento-document_by_user',
    ),
    path(
        'api/agregar/documento',
        views.CrearDocumentos.as_view(),
        name='crear-documento-cliente',
    ),       
]