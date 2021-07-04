#django
from django.urls import include, path, re_path
#local
from . import views

#app_name = "users_app"

urlpatterns = [    
    path(
        'api/usuarios/<valor>',
        views.ListarTipoUsuarios.as_view(),
        name='especialista-lista'
    ),           
]