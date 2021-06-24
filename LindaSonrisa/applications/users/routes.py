# Django
from django.urls import include, path

# Django REST Framework
from rest_framework.routers import DefaultRouter

# Views
#from applications.users import views as user_views
from . import viewsets

from . import views

#app_name = 'router_users'

router = DefaultRouter()
#luego de la r es la direccion url
router.register(r'api/users/iniciar', viewsets.UserViewSet, basename='users')
router.register(r'api/amins/create', viewsets.CrearViewSet, basename='users-create')
router.register(r'api/users/create', viewsets.CrearClienteViewSet, basename='users-create')

urlpatterns = router.urls