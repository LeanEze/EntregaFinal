from django.shortcuts import render
from django.http import HttpResponse

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