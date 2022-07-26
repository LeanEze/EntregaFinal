from django.contrib import admin
from django.urls import path
from mi_app import views
from mi_app.views import mostrar_inicio


urlpatterns = [
    path('admin/', admin.site.urls),
    path('inicio/', mostrar_inicio, name='inicio'),


]