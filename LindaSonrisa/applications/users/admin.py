from django.contrib import admin
from django.utils.html import format_html
from .models import User

class UserAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'email',
        'tipo_usuario',
        'avatar',
        #'fotos'
        
        
    )
    search_fields = ['rut','nombre']
    #
    list_filter = ('tipo_usuario','especialidades')
    #
    # def fotos(self, obj):        
    #     return format_html('<img src={} width="50" height="50" />', obj.avatar.url )

admin.site.register(User, UserAdmin)