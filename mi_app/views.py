from django.shortcuts import render
from django.http import HttpResponse

def mostrar_inicio(request):
    
    return render(request ,"mi_app/index.html", {}) #templeteIndex

