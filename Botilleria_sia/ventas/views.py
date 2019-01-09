from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from datetime import datetime
from .models import DETALLE, VENTA, TipoPago
from .forms import VentaForm, DetalleForm

def index(request):
    ventas = VENTA.objects.filter(FECHA__lte=datetime.now()).order_by('-FECHA')
    nompag = 'Ventas'
    return render(request, 'ventas/index.html', locals())

# Todas las ventas
def ventas(request):
    ventas = VENTA.objects.filter(FECHA__lte=datetime.now()).order_by('-FECHA')
    return render(request, 'ventas/index.html', {'ventas': ventas})

# Lista de meses
def ventas_month(request):
    ventas = VENTA.objects.filter(FECHA__lte=datetime.now()).order_by('-FECHA')
    years = []
    for venta in ventas:
        if venta.FECHA.year not in years:
            years.append(venta.FECHA.year)
    months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    nompag = 'Ventas por mes'
    return render(request, 'ventas/ventas_month.html', locals())

# Ventas por meses
def venta_month(request, year, month):
    ventas = VENTA.objects.filter(FECHA__year=year, FECHA__month=month).order_by('-FECHA')
    year = year
    month = month
    nompag = 'Ventas por mes'
    return render(request, 'ventas/venta_month.html', locals())

# Lista de años
def ventas_year(request):
    ventas = VENTA.objects.filter(FECHA__lte=datetime.now()).order_by('-FECHA')
    years = []
    for venta in ventas:
        if venta.FECHA.year not in years:
            years.append(venta.FECHA.year)
    nompag = 'Ventas por año'
    return render(request, 'ventas/ventas_year.html', locals())

# Ventas por años
def venta_year(request, year):
    ventas = VENTA.objects.filter(FECHA__year=year).order_by('-FECHA')
    year = year
    nompag = 'Ventas por año'
    return render(request, 'ventas/venta_year.html', locals())

# Muestra una venta y sus detalles
def venta_detail(request, pk):
    venta = get_object_or_404(VENTA, pk=pk)
    detalles = DETALLE.objects.filter(NUMERO_DE_VENTA=venta.VENTA_ID)
    nompag = 'Venta N° '+str(venta.VENTA_ID)
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
    nompag = 'Añadir venta'
    return render(request, 'ventas/venta_edit.html', locals())

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
    nompag = 'Añadir producto'
    return render(request, 'ventas/detalle_edit.html', locals())

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
    nompag = 'Editar producto'
    return render(request, 'ventas/detalle_edit.html', locals())

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
    nompag = 'Editar venta'
    return render(request, 'ventas/venta_edit.html', locals())

# Eliminar un producto de una venta
def detalle_delete(request, pk):
    detalle = get_object_or_404(DETALLE, pk=pk)
    if request.method == 'POST':
        prikey = detalle.NUMERO_DE_VENTA.VENTA_ID
        detalle.delete()
        return redirect('venta_detail', pk=prikey)
    nompag = 'Eliminar producto'

    return render(request, 'ventas/detalle_delete.html', locals())

# Elimina una venta
def venta_delete(request, pk):
    venta = get_object_or_404(VENTA, pk=pk)
    if request.method == 'POST':
        venta.delete()
        return redirect('/ventas')
    nompag = 'Eliminar venta'

    return render(request, 'ventas/venta_delete.html', locals())