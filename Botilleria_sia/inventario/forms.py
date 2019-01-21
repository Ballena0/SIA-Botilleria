from django import forms
from .models import Pedido, IngresoProducto, PRODUCTO, FORMATO, PROVEEDOR


class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ('PROVEEDOR',)
        labels = {
            'PROVEEDOR':'Proveedor',
        }

class IngresoForm(forms.ModelForm):
    class Meta:
        model = IngresoProducto
        fields = ('PRODUCTO', 'CANTIDAD',)
        labels = {
            'PRODUCTO':'Producto',
            'CANTIDAD':'Cantidad',
        }

class ProductoForm(forms.ModelForm):
    class Meta:
        model = PRODUCTO
        fields = ('FORMAT_PROD', 'NOMBRE_PROD', 'PRECIO',)
        labels = {
            'FORMAT_PROD':'Formato producto',
            'NOMBRE_PROD':'Nombre producto',
            'PRECIO':'Precio $:',
        }

class NewProductoForm(forms.ModelForm):
    class Meta:
        model = PRODUCTO
        fields = ('FORMAT_PROD', 'NOMBRE_PROD', 'PRECIO',)
        labels = {
            'FORMAT_PROD': 'Formato producto',
            'NOMBRE_PROD': 'Nombre producto',
            'PRECIO': 'Precio $:',
        }


class EditProductoForm(forms.ModelForm):
    class Meta:
        model = PRODUCTO
        fields = ('PRECIO',)
        labels = {
            'PRECIO':'Precio $:',
        }

class NuevoFormatoForm(forms.ModelForm):
    class Meta:
        model = FORMATO
        fields = ('UNIDADES', 'DESCRIPCION_FOR',)
        labels = {
            'UNIDADES':'Unidades',
            'DESCRIPCION_FOR':'Unidades-CC',
        }

class NuevoProveedorForm(forms.ModelForm):
    class Meta:
        model = PROVEEDOR
        fields = ('RUT','NOMBRE','TELEFONO',)
        labels = {
            'RUT':'R.U.T',
            'NOMBRE':'Nombre proveedor',
            'TELEFONO':'N° Telefonico',
        }