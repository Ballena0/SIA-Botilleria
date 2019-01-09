from django.shortcuts import render, get_object_or_404, redirect
from datetime import datetime
from .models import PRODUCTO, Pedido, IngresoProducto
from .forms import PedidoForm, IngresoForm
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

# Todos los pedidos
def pedidos(request):
    pedidos = Pedido.objects.filter(FECHA__lte=datetime.now()).order_by('-FECHA')
    nompag = 'Pedidos'
    return render(request, 'inventario/pedidos.html', locals())

# Ingresar nuevo pedido
def pedido_new(request):
    if request.method == "POST":
        form = PedidoForm(request.POST)
        if form.is_valid():
            pedido = form.save(commit=False)
            pedido.INGRESADO_POR = request.user
            pedido.FECHA = datetime.now()
            pedido.save()
            return redirect('pedido_detail', pk=pedido.pk)
    else:
        form = PedidoForm()
    nompag = 'Ingresar pedido'
    return render(request, 'inventario/pedido_edit.html', locals())

# Editar pedido
def pedido_edit(request, pk):
    pedido = get_object_or_404(Pedido, pk=pk)
    if request.method == "POST":
        form = PedidoForm(request.POST, instance=pedido)
        if form.is_valid():
            pedido = form.save(commit=False)
            pedido.save()
            return redirect('pedido_detail', pk=pedido.PEDIDO_ID)
    else:
        form = PedidoForm(instance=pedido)
    nompag = 'Editar pedido'
    return render(request, 'inventario/pedido_edit.html', locals())

# Muestra un pedido y los productos ingresados
def pedido_detail(request, pk):
    pedido = get_object_or_404(Pedido, pk=pk)
    ingresos = IngresoProducto.objects.filter(NUMPEDIDO=pedido.PEDIDO_ID)
    nompag = 'Pedido N° '+str(pedido.PEDIDO_ID)
    return render(request, 'inventario/pedido_detail.html', locals())

# Elimina un pedido
def pedido_delete(request, pk):
    pedido = get_object_or_404(Pedido, pk=pk)
    if request.method == 'POST':
        pedido.delete()
        return redirect('pedidos')
    nompag = 'Eliminar pedido'

    return render(request, 'inventario/pedido_delete.html', locals())

# Añadir un ingreso de producto
def ingreso_new(request, pk):
    pedido = get_object_or_404(Pedido, pk=pk)
    if request.method == "POST":
        form = IngresoForm(request.POST)
        if form.is_valid():
            ingreso = form.save(commit=False)
            ingreso.NUMPEDIDO = Pedido.objects.get(PEDIDO_ID=pk)
            ingreso.save()
            return redirect('pedido_detail', pk=ingreso.NUMPEDIDO.PEDIDO_ID)
    else:
        form = IngresoForm()
    nompag = 'Ingresar producto'
    return render(request, 'inventario/ingreso_edit.html', locals())

# Editar un ingreso de producto (cambio de producto y/o cantidad)
def ingreso_edit(request, pk):
    ingreso = get_object_or_404(IngresoProducto, pk=pk)
    if request.method == "POST":
        form = IngresoForm(request.POST, instance=ingreso)
        if form.is_valid():
            ingreso = form.save(commit=False)
            ingreso.save()
            return redirect('ingreso_detail', pk=ingreso.NUMPEDIDO.PEDIDO_ID)
    else:
        form = IngresoForm(instance=ingreso)
    nompag = 'Editar ingreso'
    return render(request, 'inventario/ingreso_edit.html', locals())

# Eliminar un ingreso de producto
def ingreso_delete(request, pk):
    ingreso = get_object_or_404(IngresoProducto, pk=pk)
    if request.method == 'POST':
        prikey = ingreso.NUMPEDIDO.PEDIDO_ID
        ingreso.delete()
        return redirect('pedido_detail', pk=prikey)
    nompag = 'Eliminar ingreso'

    return render(request, 'inventario/ingreso_delete.html', locals())
