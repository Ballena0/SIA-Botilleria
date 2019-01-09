from django import forms
from .models import Pedido, IngresoProducto

class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ('PROVEEDOR',)

class IngresoForm(forms.ModelForm):
    class Meta:
        model = IngresoProducto
        fields = ('PRODUCTO', 'CANTIDAD', 'DESCRIPCION',)

