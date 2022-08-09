from django.contrib import admin
from mi_app.models import Adopcion, Donaciones, Transito
from .models import Perfil

admin.site.register(Adopcion)
admin.site.register(Transito)
admin.site.register(Donaciones)

@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'bio', 'web')