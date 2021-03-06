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
    ),
    path(
        'api/eliminar/agenda/hora/<pk>',
        views.EliminarHora.as_view(),
        name='eliminar-agenda-hora',
    ),
    path(
        'api/tomar/hora',
        views.TomarHora.as_view(),
        name='agregar-hora-paciente',
    ),
    path(
        'api/listar/hora',
        views.ListHoraPaciente.as_view(),
        name='listar-hora-paciente',
    ),
    path(
        'api/listar/horas',
        views.ListHoras.as_view(),
        name='listar-horas',
    ),

    ###
    path(
        'api/listar/especialistas',
        views.ListarEspecialistas.as_view(),
        name='listar-especialistas',
    ),
    path(
        'api/listar/agenda/especialista/<pk>',
        views.ListHorasEsp.as_view(),
        name='listar-horas-disponibles',
    ),
    path(
        'api/listar/especialistas/especialidades/<pk>',
        views.ListEspecialidades.as_view(),
        name='listar-especialistas-especialidades',
    ),


]    