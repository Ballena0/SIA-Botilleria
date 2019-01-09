from django.contrib import admin

# Register your models here.

from .models import FORMATO, PRODUCTO, PROVEEDOR, Pedido, IngresoProducto

class FormatoAdmin(admin.ModelAdmin):
    fields = ['UNIDADES', 'DESCRIPCION_FOR']
    list_display = ('UNIDADES', 'DESCRIPCION_FOR')

admin.site.register(FORMATO, FormatoAdmin)

class ProductoAdmin(admin.ModelAdmin):
    fields = ['FORMAT_PROD', 'NOMBRE_PROD', 'PRECIO', 'STOCK']
    list_display = ('NOMBRE_PROD', 'FORMAT_PROD', 'PRECIO', 'STOCK')

admin.site.register(PRODUCTO, ProductoAdmin)

class ProveedorAdmin(admin.ModelAdmin):
    fields = ['NOMBRE', 'RUT', 'TELEFONO']
    list_display = ('NOMBRE', 'RUT', 'TELEFONO')

admin.site.register(PROVEEDOR, ProveedorAdmin)

class PedidoAdmin(admin.ModelAdmin):
    fields = ['PROVEEDOR', 'FECHA', 'INGRESADO_POR']
    list_display = ('PROVEEDOR', 'FECHA', 'INGRESADO_POR')

admin.site.register(Pedido, PedidoAdmin)

class IngresoAdmin(admin.ModelAdmin):
    fields = ['NUMPEDIDO', 'PRODUCTO', 'CANTIDAD', 'DESCRIPCION']
    list_display = ('NUMPEDIDO', 'PRODUCTO', 'CANTIDAD', 'DESCRIPCION')

admin.site.register(IngresoProducto, IngresoAdmin)
