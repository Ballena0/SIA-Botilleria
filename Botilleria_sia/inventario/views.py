from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    context = {}
    return render(request, 'inventario/base.html', context)

def productos(request):
    return render(request, 'inventario/productos.html')

def tipo_formato(request):
    context = {}
    return render(request,'inventario/tipoformato.html', context)

