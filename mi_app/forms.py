from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class adopcionFormulario(forms.Form):

    nombre= forms.CharField(max_length=40, label="¿Cual es tu nombre?", required=True)
    apellido = forms.CharField(max_length=40, label="¿Cual es tu apellido?", required=True)
    edad = forms.IntegerField(label="¿Cual es tu edad?")
    email = forms.EmailField(max_length=40, label="¿cual es tu Email?", required=True)
    telefono = forms.CharField(max_length=40, label="¿Cual es tu numero de telefono?", required=True)
    cantidadIntegrantesFamilia = forms.IntegerField(label="¿Cuantas personas conforman tu familia?")
    tamañoAnimal = forms.CharField(max_length=40, label="¿Que tamaño prefiere del animal?", required=True)
    animalInteresado = forms.CharField(max_length=40, label="¿Alguno de los animales de las redes le ha interesado?", required=True)
    localidad = forms.CharField(max_length=100)
    direccion = forms.CharField(max_length=100)
    tamañoVivienda = forms.CharField(max_length=40, label="¿Cuantos hambientes tiene su vivienda?", required=True)
    patioVivienda = forms.CharField(max_length=40, label="¿La vivienda cuenta con patio/balcon/parque?", required=True)
    

class transitoFormulario(forms.Form):

    nombre= forms.CharField(max_length=40, label="¿Cual es tu nombre?", required=True)
    apellido = forms.CharField(max_length=40, label="¿Cual es tu apellido?", required=True)
    edad = forms.IntegerField(label="¿Cual es tu edad?")
    email = forms.EmailField(max_length=40, label="¿cual es tu Email?", required=True)
    telefono = forms.CharField(max_length=40, label="¿Cual es tu numero de telefono? (Indicar prefijo de la zona)", required=True)
    perros = forms.CharField(max_length=2, label="¿Tiene perro/s?", required=True)
    gatos = forms.CharField(max_length=2, label="¿Tiene gato/s?", required=True)
    niños = forms.CharField(max_length=40, label="¿Hay niños con los que tendria contacto el animal?", required=True)
    localidad = forms.CharField(max_length=100)
    direccion = forms.CharField(max_length=100)
    hambientes = forms.IntegerField(label="¿Cuantos hambientes tiene su vivienda?", required=True)
    patio = forms.CharField(max_length=40, label="¿La vivienda cuenta con patio/balcon/parque?", required=True)


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



