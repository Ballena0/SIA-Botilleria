from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from inventario.models import PRODUCTO


def index(request):
    context = {}
    return render(request, 'base.html', context)

def productos(request, ID_PROD):
    producto = PRODUCTO.objects.get(pk=ID_PROD)
    context = { producto }
    return render(request, 'productos.html', context)

def tipo_formato(request):
    context = {}
    return render(request,'tipoformato.html', context)