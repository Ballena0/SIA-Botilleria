from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import *


def index(request):
    context = {}
    return render(request, 'base.html', context)

def productos(request):
    ##producto = PRODUCTO.objects.get(pk=ID_PROD)
    ##context = {producto}
    return render(request, 'productos.html')

def tipo_formato(request):
    context = {}
    return render(request,'tipoformato.html', context)