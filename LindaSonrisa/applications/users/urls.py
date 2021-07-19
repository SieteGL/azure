#django
from django.urls import include, path, re_path
#local
from . import views

#app_name = "users_app"

urlpatterns = [    
    path(
        'api/usuarios/<valor>',
        views.ListarTipoUsuarios.as_view(),
        name='usuarios-lista'
    ),
    path(
        'api/administrador/sistema',
        views.ListarAdministradores.as_view(),
        name='usuarios-admin-todos'
    ),                
    path(
        'api/especialistas/sistema',
        views.ListarEspecialistas.as_view(),
        name='usuarios-espe-todos'
    ),                
    path(
        'api/recepcionistas/sistema',
        views.ListarRecepcionista.as_view(),
        name='usuarios-recep-todos'
    ),                
    path(
        'api/cliente/sistema',
        views.ListarClientes.as_view(),
        name='usuarios-client-todos'
    ),                
    path(
        'api/proveedores/sistema',
        views.ListarProveedores.as_view(),
        name='usuarios-provee-todos'
    ),
    path(
        'api/token/',
        views.CustomTokenObtainPairView.as_view(), 
     name='token_obtain_pair'),
    ###PRUEBA
    #                 
    # path(
    #     'api/update/admin/<pk>',
    #     views.UpdateUser.as_view(),
    #     name='update-admin'
    # ),                
                   
]