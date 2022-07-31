from django.shortcuts import render
from django.http import HttpResponse

# funciones de muestra de template del header
def mostrar_inicio(request):
    
    return render(request ,"mi_app/index.html", {}) #templete Index

def mostrar_formulario_adopcion(request):
    
    return render(request ,"mi_app/formularioAdopcion.html", {}) #templete Adopcion

def mostrar_transito(request):
    
    return render(request ,"mi_app/transitar.html", {}) #templete transito


def mostrar_donaciones(request):
    
    return render(request ,"mi_app/donaciones.html", {}) #templete Donaciones

def ingresar_usuario(request):
    
    return render(request ,"mi_app/ingresarUsuario.html", {})




# funciones de muestra de template de historias

def mostrar_aisha(request):
    
    return render(request ,"mi_app/historias/aisha.html", {}) #templete historias aisha

def mostrar_anubis(request):
    
    return render(request ,"mi_app/historias/anubis.html", {}) #templete historias anubis

def mostrar_canela(request):
    
    return render(request ,"mi_app/historias/canela.html", {}) #templete historias canela

def mostrar_carl(request):
    
    return render(request ,"mi_app/historias/carl.html", {}) #templete historias carl

def mostrar_lucas(request):
    
    return render(request ,"mi_app/historias/lucas.html", {}) #templete historias lucas

def mostrar_osito(request):
    
    return render(request ,"mi_app/historias/osito.html", {}) #templete historias osito

def mostrar_pantufla(request):
    
    return render(request ,"mi_app/historias/pantufla.html", {}) #templete historias pantufla

def mostrar_romarubio(request):
    
    return render(request ,"mi_app/historias/romarubio.html", {}) #templete historias romarubio




