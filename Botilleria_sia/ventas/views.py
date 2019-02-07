from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from datetime import datetime
from .models import DETALLE, VENTA, TipoPago
from .forms import VentaForm, DetalleForm, VentaFechaForm, VentaDayForm
import json
from django.core import serializers

# Página principal de ventas
def index(request):
    ventas = VENTA.objects.filter(FECHA__lte=datetime.now()).order_by('-FECHA')
    nompag = 'Ventas'
    month = datetime.now().month
    if month == 1 or month == 3 or month == 4 or month == 7 or month == 8 or month == 10 or month == 12:
        dias = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]
        numventas = []
        ingresos = []
        for dia in dias:
            count = 0
            ingr = 0
            for venta in ventas:
                if venta.FECHA.year == datetime.now().year and venta.FECHA.month == month and venta.FECHA.day == dia and venta.ESTADO == True:
                    ingr = ingr + venta.TOTAL_A_PAGAR
                    count = count + 1
            numventas.append(count)
            ingresos.append(ingr)
    elif month == 4 or month == 6 or month == 9 or month == 11:
        dias = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
        numventas = []
        ingresos = []
        for dia in dias:
            count = 0
            ingr = 0
            for venta in ventas:
                if venta.FECHA.year == datetime.now().year and venta.FECHA.month == month and venta.FECHA.day == dia and venta.ESTADO == True:
                    ingr = ingr + venta.TOTAL_A_PAGAR
                    count = count + 1
            numventas.append(count)
            ingresos.append(ingr)
    else:
        for venta in ventas:
            if venta.FECHA.year%4 == 0 and venta.FECHA.year%100 != 0 and venta.FECHA.year%400 == 0:
                dias = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]
            elif venta.FECHA.year%4 != 0:
                dias = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28]
        numventas = []
        ingresos = []
        for dia in dias:
            count = 0
            ingr = 0
            for venta in ventas:
                if venta.FECHA.year == datetime.now().year and venta.FECHA.month == month and venta.FECHA.day == dia and venta.ESTADO == True:
                    ingr = ingr + venta.TOTAL_A_PAGAR
                    count = count + 1
            numventas.append(count)
            ingresos.append(ingr)
    dias = json.dumps(dias)
    numventas = json.dumps(numventas)
    return render(request, 'ventas/index.html', locals())

# Todas las ventas
def ventas(request):
    ventas = VENTA.objects.filter(FECHA__lte=datetime.now()).order_by('-FECHA')
    nompag = 'Todas las ventas'
    return render(request, 'ventas/ventas.html', locals())

# Ventas por rango de fecha
def daterange(request):
    if request.method == "POST":
        form = VentaFechaForm(request.POST)
        if form.is_valid():
            start_date = form.cleaned_data['Fecha_inicial']
            end_date = form.cleaned_data['Fecha_final']
            ventas = VENTA.objects.filter(FECHA__range=[start_date, end_date])
            if ventas:
                rec = 0
                for venta in ventas:
                    if venta.ESTADO:
                        rec = rec + venta.TOTAL_A_PAGAR
            else:
                error = True
                form = VentaFechaForm()
    else:
        form = VentaFechaForm()
    nompag = 'Ventas por rango de fecha'
    return render(request, 'ventas/daterange.html', locals())


# Ventas por días
def ventas_day(request):
    hoy = datetime.today()
    if request.method == "POST":
        form = VentaDayForm(request.POST)
        if form.is_valid():
            fecha = form.cleaned_data['Fecha']
            ventas = VENTA.objects.filter(FECHA=fecha)
            if ventas:
                rec = 0
                for venta in ventas:
                    year = venta.FECHA.year
                    month = venta.FECHA.month
                    day = venta.FECHA.day
                    if venta.ESTADO:
                        rec = rec + venta.TOTAL_A_PAGAR
                return redirect('venta_day', year, month, day)
            else:
                error = True
                form = VentaDayForm()
    else:
        form = VentaDayForm()
    nompag = 'Ventas por día'
    return render(request, 'ventas/ventas_day.html', locals())

# Escoger fecha para venta por día
def venta_day(request, year, month, day):
    ventas = VENTA.objects.filter(FECHA__year=year, FECHA__month=month, FECHA__day=day).order_by('-FECHA')
    year = year
    month = month
    day = day
    rec = 0
    for venta in ventas:
        if venta.ESTADO:
            rec = rec + venta.TOTAL_A_PAGAR
    nompag = 'Ventas por día'
    return render(request, 'ventas/venta_day.html', locals())

# Ventas por día
def venta_day(request, year, month, day):
    ventas = VENTA.objects.filter(FECHA__year=year, FECHA__month=month, FECHA__day=day).order_by('-FECHA')
    year = year
    month = month
    day = day
    rec = 0
    for venta in ventas:
        if venta.ESTADO:
            rec = rec + venta.TOTAL_A_PAGAR
    nompag = 'Ventas por día'
    return render(request, 'ventas/venta_day.html', locals())

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
    rec = 0
    for venta in ventas:
        if venta.ESTADO:
            rec = rec + venta.TOTAL_A_PAGAR
    nompag = 'Ventas por mes'
    if month == 1 or month == 3 or month == 4 or month == 7 or month == 8 or month == 10 or month == 12:
        dias = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28,
                29, 30, 31]
        numventas = []
        ingresos = []
        for dia in dias:
            count = 0
            ingr = 0
            for venta in ventas:
                if venta.FECHA.year == year and venta.FECHA.month == month and venta.FECHA.day == dia and venta.ESTADO == True:
                    ingr = ingr + venta.TOTAL_A_PAGAR
                    count = count + 1
            numventas.append(count)
            ingresos.append(ingr)
    elif month == 4 or month == 6 or month == 9 or month == 11:
        dias = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28,
                29, 30]
        numventas = []
        ingresos = []
        for dia in dias:
            count = 0
            ingr = 0
            for venta in ventas:
                if venta.FECHA.year == datetime.now().year and venta.FECHA.month == month and venta.FECHA.day == dia and venta.ESTADO == True:
                    ingr = ingr + venta.TOTAL_A_PAGAR
                    count = count + 1
            numventas.append(count)
            ingresos.append(ingr)
    else:
        if venta.FECHA.year % 4 == 0 and venta.FECHA.year % 100 != 0 and venta.FECHA.year % 400 == 0:
            dias = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]
        elif venta.FECHA.year % 4 != 0:
            dias = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28]
        numventas = []
        ingresos = []
        for dia in dias:
            count = 0
            ingr = 0
            for venta in ventas:
                if venta.FECHA.year == datetime.now().year and venta.FECHA.month == month and venta.FECHA.day == dia and venta.ESTADO == True:
                    ingr = ingr + venta.TOTAL_A_PAGAR
                    count = count + 1
            numventas.append(count)
            ingresos.append(ingr)
    dias = json.dumps(dias)
    numventas = json.dumps(numventas)
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
    months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    year = year
    rec = 0
    for venta in ventas:
        if venta.ESTADO:
            rec = rec + venta.TOTAL_A_PAGAR
    numventas = []
    ingresos = []
    for month in months:
        count = 0
        ingr = 0
        for venta in ventas:
            if venta.FECHA.year == year and venta.FECHA.month == month and venta.ESTADO == True:
                ingr = ingr + venta.TOTAL_A_PAGAR
                count = count + 1
        numventas.append(count)
        ingresos.append(ingr)
    nompag = 'Ventas por año'
    numventas = json.dumps(numventas)
    return render(request, 'ventas/venta_year.html', locals())

# Muestra una venta y sus detalles
def venta_detail(request, pk):
    venta = get_object_or_404(VENTA, pk=pk)
    detalles = DETALLE.objects.filter(NUMERO_DE_VENTA=venta.VENTA_ID)
    nompag = 'Venta N° '+str(venta.VENTA_ID)
    if request.method == "POST":
        form = DetalleForm(request.POST)
        if form.is_valid():
            detalle = form.save(commit=False)
            detalle.NUMERO_DE_VENTA = VENTA.objects.get(VENTA_ID=pk)
            if detalle.PRODUCTO.STOCK >= detalle.CANTIDAD:
                detalle.totald()
                detalle.save()
                return redirect('venta_detail', pk=detalle.NUMERO_DE_VENTA.VENTA_ID)
            else:
                error = True
                producto = detalle.PRODUCTO
                stock = detalle.PRODUCTO.STOCK
                form = DetalleForm()
    else:
        form = DetalleForm()
    venta.totalv()
    return render(request, 'ventas/venta_detail.html', locals())

# Confirma el pago de una venta y bloquea los botones de edición
def venta_pago(request, pk):
    venta = get_object_or_404(VENTA, pk=pk)
    detalles = DETALLE.objects.filter(NUMERO_DE_VENTA=venta.VENTA_ID)
    venta.estado()
    for detalle in detalles:
        if detalle.ESTADO == False:
            detalle.stockd()
            detalle.ESTADO = True
            detalle.save()
    nompag = 'Venta N° ' + str(venta.VENTA_ID)
    return render(request, 'ventas/venta_detail.html', locals())

# Crear una nueva venta
def venta_new(request):
    if request.method == "POST":
        form = VentaForm(request.POST)
        if form.is_valid():
            venta = form.save(commit=False)
            if request.user.first_name and request.user.last_name:
                venta.VENDEDOR = request.user.first_name + ' ' + request.user.last_name
            else:
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
            if detalle.PRODUCTO.STOCK >= detalle.CANTIDAD:
                detalle.totald()
                detalle.save()
                return redirect('venta_detail', pk=detalle.NUMERO_DE_VENTA.VENTA_ID)
            else:
                error = True
                producto = detalle.PRODUCTO
                stock = detalle.PRODUCTO.STOCK
                form = DetalleForm()
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

# PWA
def base_layout(request):
    template = 'ventas/base.html'
    return render(request, template)

def getdata(request):
 results=feed.objects.all()
 jsondata = serializers.serialize('json',results)
 return HttpResponse(jsondata)