# django
from django.urls import include, path, re_path
# local
from . import views


app_name = "hora_app"

urlpatterns = [
    path(
        'api/listar/agenda',
        views.ListarAgenda.as_view(),
        name='agenda-listar',
    ),
    path(
        'api/crear/agenda',
        views.CrearAgenda.as_view(),
        name='agenda-crear',
    )
]    