from django.contrib import admin

# Register your models here.

from .models import FORMATO, PRODUCTO, PROVEEDOR

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
