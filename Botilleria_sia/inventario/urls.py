from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('productos/', views.productos, name='productos'),
    path('tipoformato/', views.tipo_formato, name='tipoformato')
]