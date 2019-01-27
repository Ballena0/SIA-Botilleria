from django.urls import path, include
from . import views

urlpatterns = [
    path('ventas/', views.index, name='index'),
    path('ventas/ventas/', views.ventas, name='ventas'),
    path('ventas/daterange/', views.daterange, name='daterange'),
    path('ventas/year/', views.ventas_year, name='ventas_year'),
    path('ventas/year/<int:year>', views.venta_year, name='venta_year'),
    path('ventas/month/', views.ventas_month, name='ventas_month'),
    path('ventas/year/<int:year>/month/<int:month>', views.venta_month, name='venta_month'),
    path('ventas/day/', views.ventas_day, name='ventas_day'),
    path('ventas/year/<int:year>/month/<int:month>/day/<int:day>', views.venta_day, name='venta_day'),
    path('ventas/venta/<int:pk>/', views.venta_detail, name='venta_detail'),
    path('ventas/venta/<int:pk>/pago-realizado', views.venta_pago, name='venta_pago'),
    path('ventas/venta/new', views.venta_new, name='venta_new'),
    path('ventas/detalle/new/<int:pk>', views.detalle_new, name='detalle_new'),
    path('ventas/detalle/<int:pk>/edit/', views.detalle_edit, name='detalle_edit'),
    path('ventas/venta/<int:pk>/edit/', views.venta_edit, name='venta_edit'),
    path('ventas/detalle/<int:pk>/delete/', views.detalle_delete, name='detalle_delete'),
    path('ventas/venta/<int:pk>/delete/', views.venta_delete, name='venta_delete'),
    path(r'base_layout', views.base_layout, name='base_layout'),
]

