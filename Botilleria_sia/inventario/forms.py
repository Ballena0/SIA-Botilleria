from django import forms
from .models import Pedido, IngresoProducto, PRODUCTO, FORMATO, PROVEEDOR


class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ('PROVEEDOR',)


class IngresoForm(forms.ModelForm):
    class Meta:
        model = IngresoProducto
        fields = ('PRODUCTO', 'CANTIDAD',)


class ProductoForm(forms.ModelForm):
    class Meta:
        model = PRODUCTO
        fields = ('FORMAT_PROD', 'NOMBRE_PROD', 'PRECIO',)


class NewProductoForm(forms.ModelForm):
    class Meta:
        model = PRODUCTO
        fields = ('FORMAT_PROD', 'NOMBRE_PROD', 'PRECIO',)


class EditProductoForm(forms.ModelForm):
    class Meta:
        model = PRODUCTO
        fields = ('PRECIO',)


class NuevoFormatoForm(forms.ModelForm):
    class Meta:
        model = FORMATO
        fields = ('UNIDADES', 'DESCRIPCION_FOR',)

class NuevoProveedorForm(forms.ModelForm):
    class Meta:
        model = PROVEEDOR
        fields = ('RUT','NOMBRE','TELEFONO',)