from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('productos/', views.productos, name='productos'),
    path('tipoformato/', views.tipo_formato, name='tipoformato'),
    path('pedidos/', views.pedidos, name='pedidos'),
    path('pedido/new', views.pedido_new, name='pedido_new'),
    path('pedido/<int:pk>/', views.pedido_detail, name='pedido_detail'),
    path('pedido/<int:pk>/pedido-ingresado', views.pedido_ingresado, name='pedido_ingresado'),
    path('pedido/<int:pk>/edit/', views.pedido_edit, name='pedido_edit'),
    path('pedido/<int:pk>/delete/', views.pedido_delete, name='pedido_delete'),
    path('ingreso/new/<int:pk>', views.ingreso_new, name='ingreso_new'),
    path('ingreso/<int:pk>/edit/', views.ingreso_edit, name='ingreso_edit'),
    path('ingreso/<int:pk>/delete/', views.ingreso_delete, name='ingreso_delete'),
    path('producto/nuevoprod/', views.new_producto, name='new_producto'),
    path('producto/<int:pk>/delete', views.producto_delete, name='producto_delete'),
    path('producto/<int:pk>/precio_edit', views.precio_edit, name='precio_edit'),
    path('proveedor/', views.prov_new, name='prov_new'),
]