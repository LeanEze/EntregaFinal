from django.contrib import admin
from django.urls import path,include
from mi_app import views
from mi_app.views import adopcion_formulario, ingresar_usuario, mostrar_inicio, mostrar_donaciones, crear_usuario, respuesta_adopcion, respuesta_transito, transito_formulario
from mi_app.views import password_reset, password_reset_confirm, password_reset_done, password_reset_complete
from mi_app.views import adopcion_formulario, donaciones_formulario, ingresar_usuario, mostrar_inicio, crear_usuario, respuesta_adopcion, respuesta_donaciones, respuesta_transito, transito_formulario








urlpatterns = [
    path('admin/', admin.site.urls),
    #rutas header
    path('inicio/', mostrar_inicio, name='inicio'),
    path('adoptar/', adopcion_formulario, name='adoptar'),
    path('transitar/', transito_formulario, name='transito'),
    path('donaciones/', donaciones_formulario, name='donaciones'),
    path('ingresarusuario/', ingresar_usuario, name='ingresarusuario'),
    path('crearusuario/', crear_usuario, name= 'crearusuario'),
  
    
    #rutas de formularios
    path('respuestaAdopcion/', respuesta_adopcion, name='respuestaAdopcion'),
    path('respuestaTransito/', respuesta_transito, name='respuestaTransito'),
    path('respuestaDonaciones/', respuesta_donaciones, name='respuestaTransito'),
    
    #rutas a historias
    path('aisha/', views.mostrar_aisha, name='aisha'),
    path('anubis/', views.mostrar_anubis, name='anubis'),
    path('canela/', views.mostrar_canela, name='canela'),
    path('carl/', views.mostrar_carl, name='carl'),
    path('lucas/', views.mostrar_lucas, name='lucas'),
    path('osito/', views.mostrar_osito, name='osito'),
    path('pantufla/', views.mostrar_pantufla, name='pantufla'),
    path('romarubio/', views.mostrar_romarubio, name='romarubio'),
    
    #CRUD Transitantes

    #passwordResetPaths
    path('passwordReset/', views.password_reset, name='password_reset'), 

    path('passwordResetDone/', password_reset_done, name='password_reset_done'),

    #path('reset/<uidb64>[0-9A-Za-z_\-]/<token>', password_reset_confirm, name='password_reset_confirm'),

    #path('reset/done', password_reset_complete, name='password_reset_complete'),



    
    path('transitolist/', views.TransitoList.as_view(), name='List'),
    path(r'^detalle/(?P<pk>\d+)$', views.TransitoDetalle.as_view(), name='Detalle'),
    path(r'^nuevo$', views.TransitoCreacion.as_view(), name='Nuevo'),
    path(r'^editar/(?P<pk>\d+)$', views.TransitoUpdate.as_view(), name='Editar'),
    path(r'^borrar/(?P<pk>\d+)$', views.TransitoDelete.as_view(), name='Borrar'),


]
