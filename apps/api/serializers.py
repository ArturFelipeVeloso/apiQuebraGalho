from rest_framework.serializers import ModelSerializer
from .models import *

class VendedorSerializer(ModelSerializer):
    class Meta:
        model = Vendedor
        fields = ['nome', 'sexo', 'dataCriacao', 'dataAtualizacao']
    
class CategoriaSerializer(ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'
        
class ClienteSerializer(ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'
    
class ItensVendaSerializer(ModelSerializer):
    class Meta:
        model = ItensVenda
        fields = '__all__'
    
class ProdutoSerializer(ModelSerializer):
    class Meta:
        model = Produto
        fields = '__all__'
    
class VendaSerializer(ModelSerializer):
    class Meta:
        model = Venda
        fields = '__all__'