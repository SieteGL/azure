from django.conf import settings
from django.urls import include, path, re_path
from django.conf.urls.static import static
from django.contrib import admin

# REST_FRAMEWORK
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('admin/', admin.site.urls),    
    #routers app
    re_path('', include(('applications.users.routes', 'users'), namespace='users')),
    re_path('', include('applications.home.urls')),
    #probando 2 urls por app
    re_path('', include('applications.users.urls')),
    re_path('', include('applications.documentos.urls')),
    re_path('', include('applications.boleta.urls')),
    re_path('', include('applications.almacen.urls')),
    re_path('', include('applications.servicios.urls')),
    re_path('', include('applications.recepcion.urls')),
    re_path('', include('applications.hora.urls')),
    # users app Create access to different modules
    #re_path('', include('applications.users.urls')),
]
