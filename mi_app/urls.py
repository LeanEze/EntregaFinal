from django.contrib import admin
from django.urls import path,include
from mi_app import views
from mi_app.views import adopcion_formulario, ingresar_usuario, mostrar_inicio, mostrar_donaciones, mostrar_transito, crear_usuario, respuesta_formulario


urlpatterns = [
    path('admin/', admin.site.urls),
    #rutas header
    path('inicio/', mostrar_inicio, name='inicio'),
    path('adoptar/', adopcion_formulario, name='adoptar'),
    path('transitar/', mostrar_transito, name='transito'),
    path('donaciones/', mostrar_donaciones, name='donaciones'),
    path('ingresarusuario/', ingresar_usuario, name='ingresarusuario'),
    path('crearusuario/', crear_usuario, name= 'crearusuario'),
    
    #rutas de formularios
    path('respuestaformulario/', respuesta_formulario, name='respuestaformulario'),
    
    
    #rutas a historias
    path('aisha/', views.mostrar_aisha, name='aisha'),
    path('anubis/', views.mostrar_anubis, name='anubis'),
    path('canela/', views.mostrar_canela, name='canela'),
    path('carl/', views.mostrar_carl, name='carl'),
    path('lucas/', views.mostrar_lucas, name='lucas'),
    path('osito/', views.mostrar_osito, name='osito'),
    path('pantufla/', views.mostrar_pantufla, name='pantufla'),
    path('romarubio/', views.mostrar_romarubio, name='romarubio'),
    path('chocolate/', views.mostrar_chocolate, name='chocolate'),
]