from django.contrib import admin
from django.urls import path
from mi_app import views



urlpatterns = [
    path('admin/', admin.site.urls),

]