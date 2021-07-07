# django
from django.urls import include, path, re_path
# local
from . import views


app_name = "documentos_app"

urlpatterns = [
    path(
        
        #Modulo 1 crear ficha cliente
        'api/agregar/ficha',
        views.CrearFichaTecnica.as_view(),
        name='crear-ficha-cliente',
    ),
    path(

        # Modulo 2 Listar procedimiento cliente
        'api/listar/procedimiento',
        views.ListarProcedimientos.as_view(),
        name='listar-procedimiento-cliente',
    ),
    path(
        # Modulo 2
        'api/agregar/procedimiento',
        views.CrearProcedimientos.as_view(),
        name='crear-procedimiento-cliente',
    ),
    path(

        # Modulo 2
        'api/editar/Procedimiento/<pk>',
        views.EditarProcedimientos.as_view(),
        name='editar-procedimiento-cliente',
    ),
    path(
        # Modulo 2
        'api/eliminar/Procedimiento/<pk>',
        views.EliminarProcedimientos.as_view(),
        name='eliminar-procedimiento-cliente',
    ),
    path(

        #Modulo 3 Documento usuario
        'api/documentos/usuario',
        views.ListDocumentsUser.as_view(),
        name='documento-document_by_user',
    ),
    path(

        #Modulo 3
        'api/agregar/documento',
        views.CrearDocumentos.as_view(),
        name='crear-documento-cliente',
    ),
    path(
        #Modulo 3
        'api/editar/documento/<pk>',
        views.EditarDocumentos.as_view(),
        name='editar-documento-cliente',
    ),
    path(
        #Modulo 3
        'api/eliminar/documento/<pk>',
        views.DeleteDocumentos.as_view(),
        name='delete -documento-cliente',
    ),        
]