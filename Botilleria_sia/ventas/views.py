from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from datetime import datetime
from .models import DETALLE, VENTA, TipoPago
from .forms import VentaForm, DetalleForm

def index(request):
    ventas = VENTA.objects.filter(FECHA__lte=datetime.now()).order_by('FECHA')
    return render(request, 'ventas/index.html', {'ventas': ventas})

def ventas(request):
    ventas = VENTA.objects.filter(FECHA__lte=datetime.now()).order_by('FECHA')
    return render(request, 'ventas.html', {'ventas': ventas})

def detalles(request):
    detalle = DETALLE.objects.get(pk=DETALLE_ID)
    return render(request, 'detalles.html', {'detalle': detalle})

def venta_detail (request, pk):
    venta = get_object_or_404(VENTA, pk=pk)
    detalles = DETALLE.objects.filter(NUMERO_DE_VENTA=venta.VENTA_ID)
    venta.totalv()
    return render(request, 'ventas/venta_detail.html', locals())

def venta_new(request):
    if request.method == "POST":
        form = VentaForm(request.POST)
        if form.is_valid():
            venta = form.save(commit=False)
            venta.VENDEDOR = request.user
            venta.FECHA = datetime.now()
            venta.save()
            return redirect('venta_detail', pk=venta.pk)
    else:
        form = VentaForm()
    return render(request, 'ventas/venta_edit.html', {'form': form})

def detalle_new(request):
    if request.method == "POST":
        form = DetalleForm(request.POST)
        if form.is_valid():
            detalle = form.save(commit=False)
            detalle.totald()
            detalle.save()
            return redirect('venta_detail', pk=detalle.NUMERO_DE_VENTA.VENTA_ID)
    else:
        form = DetalleForm()
    return render(request, 'ventas/detalle_edit.html', {'form': form})

def detalle_edit(request, pk):
    detalle = get_object_or_404(DETALLE, pk=pk)
    if request.method == "POST":
        form = DetalleForm(request.POST, instance=detalle)
        if form.is_valid():
            detalle = form.save(commit=False)
            detalle.totald()
            detalle.save()
            return redirect('venta_detail', pk=detalle.NUMERO_DE_VENTA.VENTA_ID)
    else:
        form = DetalleForm(instance=detalle)
    return render(request, 'ventas/detalle_edit.html', {'form': form})

def venta_edit(request, pk):
    venta = get_object_or_404(VENTA, pk=pk)
    if request.method == "POST":
        form = VentaForm(request.POST, instance=venta)
        if form.is_valid():
            venta = form.save(commit=False)
            venta.save()
            return redirect('venta_detail', pk=venta.VENTA_ID)
    else:
        form = VentaForm(instance=venta)
    return render(request, 'ventas/venta_edit.html', {'form': form})