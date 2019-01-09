from django import forms
from .models import Pedido, IngresoProducto, PRODUCTO

class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ('PROVEEDOR',)

class IngresoForm(forms.ModelForm):
    class Meta:
        model = IngresoProducto
        fields = ('PRODUCTO', 'CANTIDAD', 'DESCRIPCION',)

class ProductoForm(forms.ModelForm):
    class Meta:
        model = PRODUCTO
        fields = ('FORMAT_PROD', 'NOMBRE_PROD', 'PRECIO',)