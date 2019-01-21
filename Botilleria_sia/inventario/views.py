from django.shortcuts import render, get_object_or_404, redirect
from datetime import datetime
from .models import PRODUCTO, Pedido, IngresoProducto
from .forms import PedidoForm, IngresoForm, NewProductoForm, EditProductoForm, NuevoFormatoForm, NuevoProveedorForm
from django.http import HttpResponse
# Create your views here.
from .models import PRODUCTO, PROVEEDOR

def index(request):
    context = {}
    return render(request, 'base.html', context)

#Lista de productos existentes
def productos(request):
    show_id = PRODUCTO.objects.all()
    nompag = 'Productos'
    return render(request, 'inventario/productos.html', locals())

# Nuevo producto
def new_producto(request):
    if request.method == 'POST':
        form = NewProductoForm(request.POST)
        if form.is_valid():
            nuevo = form.save(commit=False)
            nuevo.save()
            return redirect('productos')
    else:
        form = NewProductoForm()
    nompag = "Productos nuevos"
    return render(request, 'inventario/new_producto.html', locals())

#Nuevo tipo de formato
def tipo_formato(request):
    if request.method == 'POST':
        form = NuevoFormatoForm(request.POST)
        if form.is_valid():
            hola = form.save(commit=False)
            hola.save()
            return redirect('productos')
    else:
        form = NuevoFormatoForm()
    nompag = "Nuevo formato"
    return render(request,'inventario/tipoformato.html', locals())

# Productos por stock
def productos_stock(request):
    productos = PRODUCTO.objects.order_by('STOCK')
    nompag = 'Stock de productos'
    return render(request, 'inventario/productos_stock.html', locals())

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

# Confirma el ingreso y bloquea los botones de edición
def pedido_ingresado(request, pk):
    pedido = get_object_or_404(Pedido, pk=pk)
    ingresos = IngresoProducto.objects.filter(NUMPEDIDO=pedido.PEDIDO_ID)
    pedido.estado()
    for ingreso in ingresos:
        if ingreso.ESTADO == False:
            ingreso.stockp()
            ingreso.ESTADO = True
            ingreso.save()
    nompag = 'Pedido N° ' + str(pedido.PEDIDO_ID)
    return render(request, 'inventario/pedido_detail.html', locals())

# Elimina un pedido
def pedido_delete(request, pk):
    pedido = get_object_or_404(Pedido, pk=pk)
    if request.method == 'POST':
        pedido.delete()
        return redirect('pedidos')
    nompag = 'Eliminar pedido'

    return render(request, 'inventario/pedido_delete.html', locals())

##Eliminar producto del sistema
def producto_delete(request, pk):
    producto = get_object_or_404(PRODUCTO, pk=pk)
    if request.method == 'POST':
        producto.delete()
        return redirect('productos')
    nompag = 'Eliminar producto'
    return render(request, 'inventario/producto_delete.html', locals())

#Editar precio de un producto existente
def precio_edit(request, pk):
    producto = get_object_or_404(PRODUCTO, pk=pk)
    if request.method == 'POST':
        form = EditProductoForm (request.POST, instance=producto)
        if form.is_valid():
            producto = form.save(commit=False)
            form.save()
            return redirect('productos')
    else:
        form = EditProductoForm()
    return render(request, 'inventario/edit_producto.html', locals())

# Añadir un ingreso de producto
def ingreso_new(request, pk):
    pedido = get_object_or_404(Pedido, pk=pk)
    if request.method == "POST":
        form = IngresoForm(request.POST)
        if form.is_valid():
            ingreso = form.save(commit=False)
            ingreso.NUMPEDIDO = Pedido.objects.get(PEDIDO_ID=pk)
            ingreso.stockp()
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

#Ingresar un nuevo proveedor
def prov_new(request):
    if request.method == 'POST':
        form = NuevoProveedorForm(request.POST)
        if form.is_valid():
            prov = form.save(commit=False)
            prov.save()
            return redirect('productos')
    else:
        form = NuevoProveedorForm()
    nompag = " Nuevo proveedor"
    return render(request, 'inventario/new_proveedor.html', locals())

