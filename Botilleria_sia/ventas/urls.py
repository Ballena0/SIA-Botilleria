from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('ventas/', views.ventas, name='ventas'),
    path('venta/<int:pk>/', views.venta_detail, name='venta_detail'),
    path('venta/new', views.venta_new, name='venta_new'),
    path('detalle/new/<int:pk>', views.detalle_new, name='detalle_new'),
    path('detalle/<int:pk>/edit/', views.detalle_edit, name='detalle_edit'),
    path('venta/<int:pk>/edit/', views.venta_edit, name='venta_edit'),
    path('detalle/<int:pk>/delete/', views.detalle_delete, name='detalle_delete'),
    path('venta/<int:pk>/delete/', views.venta_delete, name='venta_delete')
]
