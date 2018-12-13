from django.contrib import admin

# Register your models here.

from .models import FORMATO, PRODUCTO

admin.site.register(FORMATO)
admin.site.register(PRODUCTO)
