from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class adopcionFormulario(forms.Form):

    nombre= forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    edad = forms.IntegerField()
    email = forms.EmailField(max_length=100)
    telefono = forms.CharField(max_length=40)
    cantidadIntegrantesFamilia = forms.IntegerField()
    tamañoAnimal = forms.CharField(max_length=40)
    animalInteresado = forms.CharField(max_length=40)
    localidad = forms.CharField(max_length=100)
    direccion = forms.CharField(max_length=100)
    tamañoVivienda = forms.CharField(max_length=40)
    patioVivienda = forms.CharField(max_length=40)
    

class transitoFormulario(forms.Form):

    nombre= forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    edad = forms.IntegerField()
    email = forms.EmailField(max_length=100)
    telefono = forms.CharField(max_length=40)
    perros = forms.CharField(max_length=2)
    gatos = forms.CharField(max_length=2)
    niños = forms.CharField(max_length=2)
    localidad = forms.CharField(max_length=100)
    direccion = forms.CharField(max_length=100)
    hambientes = forms.IntegerField()
    patio = forms.CharField(max_length=2)


class donacionesFormulario(forms.Form):

    nombre= forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    edad = forms.IntegerField()
    email = forms.EmailField(max_length=100)
    telefono = forms.IntegerField()
    tarjeta = forms.IntegerField()
    clave = forms.IntegerField()
    donacion= forms.FloatField()



class RegistroForm(UserCreationForm):

	class Meta:
		model = User
		fields = [
				'username',
				'first_name',
				'last_name',
				'email',
			]
		labels = {
				'username': 'Nombre de usuario',
				'first_name': 'Nombre',
				'last_name': 'Apellidos',
				'email': 'Correo',
		}


