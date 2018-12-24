from django.contrib import admin

from .models import VENTA, TIPO_PAGO, DETALLE

admin.site.register(VENTA)
admin.site.register(DETALLE)
admin.site.register(TIPO_PAGO)