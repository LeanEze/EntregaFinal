from django.contrib import admin
from django.urls import path
from mi_app import views
from mi_app.views import ingresar_usuario, mostrar_inicio, mostrar_formulario_adopcion, mostrar_donaciones, mostrar_transito


urlpatterns = [
    path('admin/', admin.site.urls),
    #rutas header
    path('inicio/', mostrar_inicio, name='inicio'),
    path('adoptar/', mostrar_formulario_adopcion, name='adoptar'),
    path('transitar/', mostrar_transito, name='transito'),
    path('donaciones/', mostrar_donaciones, name='donaciones'),
    path('ingresarusuario/', ingresar_usuario, name='ingresarusuario'),
    #rutas a historias
    path('aisha/', views.mostrar_aisha, name='aisha'),
    path('anubis/', views.mostrar_anubis, name='anubis'),
    path('canela/', views.mostrar_canela, name='canela'),
    path('carl/', views.mostrar_carl, name='carl'),
    path('lucas/', views.mostrar_lucas, name='lucas'),
    path('osito/', views.mostrar_osito, name='osito'),
    path('pantufla/', views.mostrar_pantufla, name='pantufla'),
    path('romarubio/', views.mostrar_romarubio, name='romarubio'),
]