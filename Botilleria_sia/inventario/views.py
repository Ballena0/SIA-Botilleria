from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import PRODUCTO, PROVEEDOR, RegistroBodega

def index(request):
    context = {}
    return render(request, 'inventario/base.html', context)

def productos(request):
    show_id= PRODUCTO.objects.all()
    return render(request, 'inventario/productos.html', {'show_id': show_id})

def tipo_formato(request):
    context = {}
    return render(request,'inventario/tipoformato.html', context)

