from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('acercade', views.acerca_de, name='acercade'),
    path('categoria/<int:id>', views.categoria, name='categoria'),
    path('buscar', views.buscar, name='buscar'),
    path('productos', views.productos, name='productos'),
    path('producto_nuevo', views.producto_nuevo, name='producto_nuevo'),
    path('producto_editar/<int:id>', views.producto_editar, name='producto_editar'),
    path('producto_borrar/<int:id>', views.producto_borrar, name='producto_borrar'),
    path('producto/<int:id>', views.producto, name='producto'),
    path('agregar_al_carrito/<int:id>', views.agregar_al_carrito, name='agregar_al_carrito'),
    path('ver_carrito', views.ver_carrito, name='ver_carrito'),
    path('eliminar_item_carrito/<int:id>', views.eliminar_item_carrito, name='eliminar_item_carrito'),
    path('vaciar_carrito', views.vaciar_carrito, name='vaciar_carrito')
]
