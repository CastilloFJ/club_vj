from django.contrib import admin
from catalogo.models import Plataforma, Genero, VideoJuego, UserProfile
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin # Agregado 
from django.contrib.auth.models import User # Agregado 

# Register your models here.
#admin.site.register(Plataforma)
#admin.site.register(Genero)
#admin.site.register(VideoJuego)

#Modificación
@admin.register(VideoJuego)
class VideoJuegoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'annio', 'plataforma', 'genero')
    list_filter = ('plataforma', 'genero', 'annio') # Este es el requisito del PDF
    search_fields = ('titulo',)

# Define un administrador "en línea" para el perfil
class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'Perfiles de Usuario'

# Define un nuevo administrador para el modelo User
class UserAdmin(BaseUserAdmin):
    inlines = (UserProfileInline,)
    list_display = ('username', 'email', 'first_name', 'last_name', 'get_vip')

    def get_vip(self, instance):
        return instance.userprofile.vip
    
    get_vip.short_description = '¿Es VIP?'
    get_vip.boolean = True

# Re-registrar User y registrar los simples
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Plataforma)
admin.site.register(Genero)