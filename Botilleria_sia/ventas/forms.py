from django import forms
from datetime import date
from .models import VENTA, DETALLE


class VentaForm(forms.ModelForm):
    class Meta:
        model = VENTA
        fields = ('TIPO_PAGO',)
        labels = {
            'TIPO_PAGO':'Tipo de pago',
        }

class DetalleForm(forms.ModelForm):
    class Meta:
        model = DETALLE
        fields = ('PRODUCTO', 'CANTIDAD',)
        labels = {
            'PRODUCTO':'Producto',
            'CANTIDAD':'Cantidad',
        }

class VentaFechaForm(forms.Form):
    Fecha_inicial = forms.DateField(widget=forms.SelectDateWidget(years=range(1990, date.today().year+10)), initial=date.today())
    Fecha_final = forms.DateField(widget=forms.SelectDateWidget(years=range(1990, date.today().year+10)), initial=date.today())

