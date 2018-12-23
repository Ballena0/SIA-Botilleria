from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('productos/', views.productos, name='productos'),
    path('tipoformato/', views.tipo_formato, name='tipoformato')
]

##correo practica verano profe sara ccastroa@sentra.cl