from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):    
    list_display = ('nome', 'descricao', 'dataCriacao', 'dataAtualizacao')
    
@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):    
    list_display = ('nome', 'categoria', 'descricao', 'precoCusto', 'precoVenda')

@admin.register(Vendedor)
class VendedorAdmin(admin.ModelAdmin):    
    list_display = ('nome', 'sexo', 'dataCriacao', 'dataAtualizacao')
    
@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):    
    list_display = ('nome', 'sexo', 'cidade', 'estado', 'pais')
    
@admin.register(Venda)
class ClienteAdmin(admin.ModelAdmin):    
    list_display = ('vendedor', 'cliente', 'formaPagamento', 'formaDivulgacao', 'statusPedido', 'dataCriacao', 'dataAtualizacao')

@admin.register(ItensVenda)
class ItensVendaAdmin(admin.ModelAdmin):    
    list_display = ('venda', 'produto', 'quantidade', 'dataCriacao', 'dataAtualizacao')
    