from django.contrib import admin
from django.urls import path
from mi_app import views
from mi_app.views import ingresar_usuario, mostrar_inicio, mostrar_formulario_adopcion, mostrar_donaciones, mostrar_transito


urlpatterns = [
    path('admin/', admin.site.urls),
    path('inicio/', mostrar_inicio, name='inicio'),
    path('adoptar/', mostrar_formulario_adopcion, name='adoptar'),
    path('transitar/', mostrar_transito, name='transito'),
    path('donaciones/', mostrar_donaciones, name='donaciones'),
    path('ingresarusuario/', ingresar_usuario, name='ingresarusuario')

]