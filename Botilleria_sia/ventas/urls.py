from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('ventas/', views.ventas, name='ventas'),
    path('venta/<int:pk>/', views.venta_detail, name='venta_detail'),
    path('venta/new', views.venta_new, name='venta_new'),
    path('detalle/new', views.detalle_new, name='detalle_new'),
    path('detalle/<int:pk>/edit/', views.detalle_edit, name='detalle_edit'),
    path('venta/<int:pk>/edit/', views.venta_edit, name='venta_edit'),
]
