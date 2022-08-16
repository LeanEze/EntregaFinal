from urllib import request
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from mi_app.forms import  AvatarFormulario, RegistroForm, UserRegisterForm, adopcionFormulario, donacionesFormulario, transitoFormulario
from mi_app.models import Adopcion, Avatar, Donaciones, Transito
from django.contrib.auth import login, authenticate
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# funciones de muestra de template del header
def mostrar_inicio(request):
    
    return render(request ,"mi_app/index.html", {}) #templete Index

def mostrar_formulario_adopcion(request):
    
    return render(request ,"mi_app/formularioAdopcion.html", {}) #templete Adopcion

def mostrar_transito(request):
    
    return render(request ,"mi_app/formularioTransito.html", {}) #templete transito

def mostrar_donaciones(request):
    
    return render(request ,"mi_app/donaciones.html", {}) #templete Donaciones

def mostrar_nosotros(request):
    
    return render(request ,"mi_app/nosotros.html", {})
#
#def ingresar_usuario(request):
    
    #return render(request ,"mi_app/ingresarUsuario.html", {})
 
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

def mostrar_chocolate(request):
    
    return render(request ,"mi_app/historias/chocolate.html", {}) #templete historias chocolate




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


#vista formularios

#####ADOPCION######
def adopcion_formulario(request):
    
    if  request.method == "POST":
        
        miFormulario = adopcionFormulario(request.POST)
        
        
        print(miFormulario)

        if miFormulario.is_valid:
           
            informacion = miFormulario.cleaned_data


            adopcion = Adopcion (nombre=informacion['nombre'], apellido=informacion['apellido'], edad=informacion['edad'], email=informacion['email'],telefono=informacion['telefono'],
            cantidadIntegrantesFamilia=informacion['cantidadIntegrantesFamilia'], tamañoAnimal=informacion['tamañoAnimal'], animalInteresado=informacion['animalInteresado'], 
            localidad=informacion['localidad'], direccion=informacion['direccion'], tamañoVivienda=informacion['tamañoVivienda'], patioVivienda=informacion['patioVivienda'])
           
            adopcion.save()

            return render(request, "mi_app/formularios/respuestaAdopcion.html",{})

   
    else:
        
        miFormulario = adopcionFormulario()
   
    return render(request, "mi_app/formularios/formularioAdopcion.html",{"miFormulario": miFormulario})


    
def respuesta_adopcion(request):
    
    return render(request ,"mi_app/formularios/respuestaAdopcion.html", {})


#####TRANSITO######


def transito_formulario(request):
    
    if  request.method == "POST":
        
        miFormulario = transitoFormulario(request.POST)
        
        
        print(miFormulario)

        if miFormulario.is_valid:
           
            informacion = miFormulario.cleaned_data


            transito = Transito (nombre=informacion['nombre'], apellido=informacion['apellido'], edad=informacion['edad'],email=informacion['email'],telefono=informacion['telefono'],
            perros=informacion['perros'], gatos=informacion['gatos'], niños=informacion['niños'], 
            localidad=informacion['localidad'], direccion=informacion['direccion'], hambientes=informacion['hambientes'], patio=informacion['patio'])
           
            transito.save()

            return render(request, "mi_app/formularios/respuestaTransito.html",{})

   
    else:
        
        miFormulario = transitoFormulario()
   
    return render(request, "mi_app/formularios/formularioTransito.html",{"miFormulario": miFormulario})


def respuesta_transito(request):
    
    return render(request ,"mi_app/formularios/respuestaTransito.html", {})



#####DONACIONES######

def donaciones_formulario(request):
    
    if  request.method == "POST":
        
        miFormulario = donacionesFormulario(request.POST)
        
        
        print(miFormulario)

        if miFormulario.is_valid:
           
            informacion = miFormulario.cleaned_data


            donaciones = Donaciones (nombre=informacion['nombre'], apellido=informacion['apellido'], edad=informacion['edad'],email=informacion['email'],telefono=informacion['telefono'],
            tarjeta=informacion['tarjeta'], clave=informacion['clave'], donacion=informacion['donacion'])
           
            donaciones.save()

            return render(request, "mi_app/formularios/respuestaDonaciones.html",{})

   
    else:
        
        miFormulario = donacionesFormulario()
   
    return render(request, "mi_app/formularios/formularioDonaciones.html",{"miFormulario": miFormulario})


def respuesta_donaciones(request):
    
    return render(request ,"mi_app/formularios/respuestaDonaciones.html", {})




#####LISTA DE TRANSITANTES POSTULADOS######



class TransitoList(ListView):

    model = Transito
    Template_name = "mi_app/transito_list.html"

class TransitoDetalle( DetailView):

    model = Transito
    template_name ="mi_app/transito_detalle1.html"

class TransitoCreacion(CreateView):
    
    model = Transito
    success_url = "/transitolist/"
    fields = ['nombre' , 'apellido']

class TransitoUpdate(UpdateView):

    model = Transito
    success_url = "/transitolist/"
    fields = ['nombre', 'apellido']

class TransitoDelete(DeleteView):

    model = Transito
    success_url = "/transitolist/"


###### CRUD USUARIO Y AVATAR ######

#LOGIN

def ingresar_usuario(request):
    
    return render(request ,"mi_app/login.html", {})
 
def crear_usuario(request):
        
    return render(request ,"mi_app/crearUsuario.html", {})





def login_request(request):
   
    if request.method == 'POST':
       
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():
            user = form.cleaned_data.get('username')
            contraseña = form.cleaned_data.get('password')

            user = authenticate(username=user, password=contraseña)

            if user is not None:                
                login(request,user)

                return render(request, "mi_app/index.html", {"mensaje":f"Bienvenido{user}"})
            else:
               
                return render(request,  "mi_app/login.html", {"mensaje":"Error, datos incorrectos"})
        else:
            
            return render(request,  "mi_app/login.html", {"mensaje":"Error, formulario incorrecto"})
    
    form = AuthenticationForm()
   
    return render(request, "mi_app/login.html", {'form':form})




def register(request):
    
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
    
        if form.is_valid():            
            username = form.cleaned_data ["username"]
            form.save()
            return render (request, "mi_app/crearUsuario.html",{"mensaje":f"{username}, Usuario Creado :)"})
    
    else: 
        form = UserRegisterForm()
       
    return render (request, "mi_app/crearUsuario.html" , {"form" : form})







class UserList(ListView,UserPassesTestMixin,):

    model = User
    Template_name = "mi_app/user_list.html"
       
    def test_func(self):
        return self.request.user.id == int(self.kwargs['pk'])


class UserDetalle(DetailView,UserPassesTestMixin):

    model = User
    template_name ="mi_app/detalleUsuario.html"

    def test_func(self):
        return self.request.user.id == int(self.kwargs['pk'])

class UserUpdate(UpdateView,UserPassesTestMixin):

    model = User
    success_url = "/userlist/"
    fields = ['username', 'email', 'last_name', 'first_name']

class UserDelete(DeleteView):

    model = User
    success_url = "/inicio/"


@login_required
def avatar(request):
    avatares = Avatar.objects.filter(user=request.user.id)
    return render(request,'mi_app/index.html',{"url":avatares[0].imagen.url})


def agregarAvatar(request):
    if request.method == 'POST':
        miFormulario = AvatarFormulario(request.POST, request.FILES)
        if miFormulario.is_valid():
            u = User.objects.get(username=request.user)
            avatar = Avatar (user=u, imagen=miFormulario.cleaned_data['imagen'])

            avatar.save()
            avatares = Avatar.objects.last()
            return render(request, "mi_app/index.html", {"url":avatares.imagen.url})

    else:
        miFormulario = AvatarFormulario()
    return render(request, "mi_app/agregarAvatar.html", {"miFormulario": miFormulario})