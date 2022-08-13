import statistics
from django.contrib import admin
from django.urls import path,include
from mi_app import views
from mi_app.views import adopcion_formulario, mostrar_inicio, mostrar_nosotros, respuesta_adopcion, respuesta_transito, transito_formulario
from mi_app.views import password_reset_done
from mi_app.views import donaciones_formulario, crear_usuario,  respuesta_donaciones
from django.contrib.auth.views import LogoutView
from django.conf.urls.static import static
from django.conf import settings




urlpatterns = [
    path('admin/', admin.site.urls),
    path('',mostrar_inicio,name='raiz'),
    #rutas header
    path('inicio/', views.mostrar_inicio, name='inicio'),
    path('adoptar/', adopcion_formulario, name='adoptar'),
    path('transitar/', transito_formulario, name='transitar'),
    path('donaciones/', donaciones_formulario, name='donaciones'),
    path('crearusuario/', crear_usuario, name= 'crearusuario'),
    path('passwordReset/', views.password_reset, name='password_reset'), 
    path('passwordResetDone/', password_reset_done, name='password_reset_done'),
    path('nosotros/', mostrar_nosotros, name='nosotros'),
     
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
    path('chocolate/', views.mostrar_chocolate, name='chocolate'),
    
    #CRUD Transitantes


    path('transitolist/', views.TransitoList.as_view(), name='List'),
    path(r'^detalle/(?P<pk>\d+)$', views.TransitoDetalle.as_view(), name='Detalle'),
    path(r'^editar/(?P<pk>\d+)$', views.TransitoUpdate.as_view(), name='Editar'),
    path(r'^borrar/(?P<pk>\d+)$', views.TransitoDelete.as_view(), name='Borrar'),


    #Login
    path('passwordReset/', views.password_reset, name='password_reset'), 
    
    
    #CrearUsuario

    path('crearusuario', views.crear_usuario, name= 'crearusuario'),
    path("login/" , views.login_request, name = "login"), 
    path("register/" , views.register, name = "register"), 
    path("logout/", LogoutView.as_view (template_name='mi_app/logout.html'), name = 'logout'),
    # path("editarusuario", views.UserUpdate.as_view(), name='editarusuario'),


    path('userlist/', views.UserList.as_view(), name='userlist'),
    path(r'^detalleuser/(?P<pk>\d+)$', views.UserDetalle.as_view(), name='userdetalle'),
    path('user/<pk>/edit', views.UserUpdate.as_view(), name='useredit'),
    path('avatar/', views.avatar, name="avatar"),
    path('agregarAvatar/', views.agregarAvatar, name="AgregarAvatar")

]
    
#para las imagenes

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)