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
 
def crear_usuario(request):
        
    return render(request ,"mi_app/crearUsuario.html", {})


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


#funciones de restablecimiento de contraseña

def password_reset(request):
    return render(request, "mi_app/passwordReset.html", {})

def password_reset_email(request):
    return render(request, "mi_app/passwordResetEmail.html", {})

def password_reset_confirm(request):
    return render(request, "mi_app/passwordResetConfirm.html", {})

def password_reset_done(request):
    return render(request, "mi_app/passwordResetDone.html", {})

def password_reset_complete(request):
    return render(request, "mi_app/passwordResetComplete.html", {})


