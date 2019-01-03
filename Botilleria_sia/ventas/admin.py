from django.contrib import admin

from .models import VENTA, TipoPago, DETALLE

class VentaAdmin(admin.ModelAdmin):
    fields = ['FECHA', 'TIPO_PAGO', 'VENDEDOR', 'TOTAL_A_PAGAR']
    list_display = ('FECHA', 'VENTA_ID', 'TIPO_PAGO', 'VENDEDOR', 'TOTAL_A_PAGAR')

admin.site.register(VENTA, VentaAdmin)

class DetalleAdmin(admin.ModelAdmin):
    fields = ['NUMERO_DE_VENTA', 'PRODUCTO', 'CANTIDAD']
    list_display = ('NUMERO_DE_VENTA', 'PRODUCTO', 'CANTIDAD', 'TOTAL_DETALLE')

admin.site.register(DETALLE, DetalleAdmin)

class TipopagoAdmin(admin.ModelAdmin):
    fields = ['TIPO_PAGO', 'PAGO_ID']
    list_display = ('TIPO_PAGO', 'PAGO_ID')

admin.site.register(TipoPago, TipopagoAdmin)