from django.db import models


class Adopcion(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    edad = models.IntegerField()
    email = models.EmailField(max_length=100)
    telefono = models.CharField(max_length=40)
    cantidadIntegrantesFamilia = models.IntegerField()
    tamañoAnimal = models.CharField(max_length=40)
    animalInteresado = models.CharField(max_length=40)
    localidad = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    tamañoVivienda = models.CharField(max_length=40)
    patioVivienda = models.CharField(max_length=40)

    def __str__(self):
    
     return f"Nombre: {self.nombre} - Apellido: {self.apellido} - Edad: {self.edad} - Telefono: {self.telefono}"



class Transito(models.Model):

    nombre= models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    edad = models.IntegerField()
    email = models.EmailField(max_length=100)
    telefono = models.CharField(max_length=40)
    perros = models.CharField(max_length=2)
    gatos = models.CharField(max_length=2)
    niños = models.CharField(max_length=2)
    localidad = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    hambientes = models.IntegerField()
    patio = models.CharField(max_length=2)


    def __str__(self):
    
     return f"Nombre: {self.nombre} - Apellido: {self.apellido} - Edad: {self.edad} - Telefono: {self.telefono}"



class Donaciones(models.Model):

    nombre= models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    edad = models.IntegerField(max_length=2)
    email = models.EmailField(max_length=100)
    telefono = models.IntegerField(max_length=40)
    tarjeta = models.IntegerField(max_length=16)
    clave = models.IntegerField(max_length=3)
    donacion= models.FloatField(max_length=10)

    def __str__(self):
    
     return f"Nombre: {self.nombre} - Apellido: {self.apellido} - donacion: {self.donacion} - Telefono: {self.telefono}"
