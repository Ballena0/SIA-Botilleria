from django import forms
from .models import VENTA, DETALLE

class VentaForm(forms.ModelForm):
    class Meta:
        model = VENTA
        fields = ('TIPO_PAGO',)

class DetalleForm(forms.ModelForm):
    class Meta:
        model = DETALLE
        fields = ('NUMERO_DE_VENTA', 'PRODUCTO', 'CANTIDAD')

