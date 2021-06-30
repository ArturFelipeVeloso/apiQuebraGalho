from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from apps.api.viewsets import *

from rest_framework import viewsets
from rest_framework.routers import SimpleRouter
from rest_framework import routers

route = routers.DefaultRouter()
route.register('categoria', CategoriaViewSet, basename='Categoria')
route.register('produto', ProdutoViewSet, basename='Produto')
route.register('vendedor', VendedorViewSet, basename='Vendedor')
route.register('cliente', ClienteViewSet, basename='Cliente')
route.register('venda', VendaViewSet, basename='Venda')
route.register('itemvenda', ItensVendaViewSet, basename='ItemVenda')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(route.urls)),
]
