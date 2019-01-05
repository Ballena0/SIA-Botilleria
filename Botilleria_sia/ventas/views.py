from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from datetime import datetime
from .models import DETALLE, VENTA, TipoPago
from .forms import VentaForm, DetalleForm

def index(request):
    ventas = VENTA.objects.filter(FECHA__lte=datetime.now()).order_by('FECHA')
    return render(request, 'ventas/index.html', {'ventas': ventas})

# Todas las ventas
def ventas(request):
    ventas = VENTA.objects.filter(FECHA__lte=datetime.now()).order_by('FECHA')
    return render(request, 'ventas/index.html', {'ventas': ventas})

# Lista de años
def ventas_year(request):
    ventas = VENTA.objects.filter(FECHA__lte=datetime.now()).order_by('FECHA')
    years = []
    for venta in ventas:
        if venta.FECHA.year not in years:
            years.append(venta.FECHA.year)
    return render(request, 'ventas/ventas_year.html', locals())

# Ventas por años
def venta_year(request, year):
    ventas = VENTA.objects.filter(FECHA__year=year).order_by('FECHA')
    return render(request, 'ventas/venta_year.html', {'ventas': ventas})

def detalles(request):
    detalle = DETALLE.objects.get(pk=DETALLE_ID)
    return render(request, 'detalles.html', {'detalle': detalle})

# Muestra una venta y sus detalles
def venta_detail (request, pk):
    venta = get_object_or_404(VENTA, pk=pk)
    detalles = DETALLE.objects.filter(NUMERO_DE_VENTA=venta.VENTA_ID)
    venta.totalv()
    return render(request, 'ventas/venta_detail.html', locals())

# Crear una nueva venta
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

# Añadir un producto a una venta
def detalle_new(request, pk):
    venta = get_object_or_404(VENTA, pk=pk)
    if request.method == "POST":
        form = DetalleForm(request.POST)
        if form.is_valid():
            detalle = form.save(commit=False)
            detalle.NUMERO_DE_VENTA = VENTA.objects.get(VENTA_ID=pk)
            detalle.totald()
            detalle.save()
            return redirect('venta_detail', pk=detalle.NUMERO_DE_VENTA.VENTA_ID)
    else:
        form = DetalleForm()
    return render(request, 'ventas/detalle_edit.html', {'form': form})

# Editar un producto en venta (cambio de producto y/o cantidad)
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

# Editar venta
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

# Eliminar un producto de una venta
def detalle_delete(request, pk):
    detalle = get_object_or_404(DETALLE, pk=pk)
    if request.method == 'POST':
        prikey = detalle.NUMERO_DE_VENTA.VENTA_ID
        detalle.delete()
        return redirect('venta_detail', pk=prikey)

    return render(request, 'ventas/detalle_delete.html', {'detalle': detalle})

# Elimina una venta
def venta_delete(request, pk):
    venta = get_object_or_404(VENTA, pk=pk)
    if request.method == 'POST':
        venta.delete()
        return redirect('/ventas')

    return render(request, 'ventas/venta_delete.html', {'venta': venta})

