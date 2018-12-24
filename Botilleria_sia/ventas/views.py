from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return HttpResponse("Página de ventas")

def ventas(request):
    venta = VENTA.objects.get(pk=VENTA_ID)
    context = { VENTA }
    return render(request, 'ventas.html', context)

def detalles(request):
    detalle = DETALLE.objects.get(pk=DETALLE_ID)
    context = { DETALLE }
    return render(request, 'detalles.html', context)

# Create your views here.
