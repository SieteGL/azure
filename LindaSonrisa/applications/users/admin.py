from django.contrib import admin

from .models import User

class UserAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'email',
        'tipo_usuario',
        #'display_tipo_usuario'
    )
    list_filter = ('tipo_usuario','especialidades')

admin.site.register(User, UserAdmin)