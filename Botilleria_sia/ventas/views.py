from django.shortcuts import render
from django.http import HttpResponse
from .models import PRODUCTO, VENTA, TIPO_PAGO

def index(request):
    return render(request, 'ventas/index.html')

def ventas(request):
    venta = VENTA.objects.get(pk=VENTA_ID)
    context = { VENTA }
    return render(request, 'ventas.html', context)

def detalles(request):
    detalle = DETALLE.objects.get(pk=DETALLE_ID)
    context = { DETALLE }
    return render(request, 'detalles.html', context)

# Create your views here.
