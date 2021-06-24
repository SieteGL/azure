#django
from django.urls import include, path, re_path
#local
from . import views

app_name = "boleta_app"

urlpatterns = [
    path(
        'api/boleta/lista',
        views.ListBoletaUser.as_view(),
        name = 'boleta-lista'
    ),
    path(
        'api/boleta/create/',
        views.CreateBoletaUser.as_view(),
        name='boleta-register'
    ),
]