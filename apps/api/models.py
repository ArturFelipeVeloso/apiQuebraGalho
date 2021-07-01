from django.db import models

# Create your models here.
class Categoria(models.Model):
    nome = models.CharField('Nome', max_length=150, null=True, blank=True)
    descricao = models.CharField('Descricao',  max_length=150, blank=True,null=True)
    
    dataCriacao = models.DateTimeField('Data de criação', auto_now_add=True)
    dataAtualizacao = models.DateTimeField('Última data de atualização', auto_now=True)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = '1 - Categorias'

    def __str__(self):
        return str(self.nome)
    
class Produto(models.Model):
    nome = models.CharField('Nome', max_length=150, null=True, blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, verbose_name="Categoria")
    descricao = models.CharField('Descricao',  max_length=250, blank=True, null=True)
    precoCusto = models.DecimalField("Preço de custo", blank=True,null=True, max_digits=10, decimal_places=2)
    precoVenda = models.DecimalField("Preço de venda", blank=True,null=True, max_digits=10, decimal_places=2)
    

    dataCriacao = models.DateTimeField('Data de criação', auto_now_add=True)
    dataAtualizacao = models.DateTimeField('Última data de atualização', auto_now=True)

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = '2 - Produtos'

    def __str__(self):
        return str(self.nome)
    
class Cliente(models.Model):
    SEXO_CHOICES = (
        ("F", "Feminino"),
        ("M", "Masculino"),
        ("N", "Nenhuma das opções")
    )
    
    nome = models.CharField('Nome', max_length=150, null=True, blank=True)
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES, blank=False, null=False)
    cidade = models.CharField('Cidade', max_length=150, null=True, blank=True)
    estado = models.CharField('Estado', max_length=150, null=True, blank=True)
    pais = models.CharField('País', max_length=150, null=True, blank=True)

    dataCriacao = models.DateTimeField('Data de criação', auto_now_add=True)
    dataAtualizacao = models.DateTimeField('Última data de atualização', auto_now=True)

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = '4 - Clientes'

    def __str__(self):
        return str(self.nome)

class Vendedor(models.Model):
    SEXO_CHOICES = (
        ("F", "Feminino"),
        ("M", "Masculino"),
        ("N", "Nenhuma das opções")
    )
    
    nome = models.CharField('Nome', max_length=150, null=True, blank=True)
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES, blank=False, null=False)

    dataCriacao = models.DateTimeField('Data de criação', auto_now_add=True)
    dataAtualizacao = models.DateTimeField('Última data de atualização', auto_now=True)

    class Meta:
        verbose_name = 'Vendedor'
        verbose_name_plural = '3 - Vendedores'

    def __str__(self):
        return str(self.nome)

class Venda(models.Model):
    PAG_CHOICES = (
        ("C", "Cartão crédito"),
        ("D", "Cartão débito"),
        ("V", "A vista"),
        ("P", "PIX"),
        ("T", "Transferência"),
        ("B", "Boleto"),
    )
    
    DIV_CHOICES = (
        ("R", "Redes sociais"),
        ("T", "TV"),
        ("I", "Indicação de amigos"),
        ("Y", "YouTube"),
    )
    
    STATUS_CHOICES = (
        ("1", "No carrinho"),
        ("2", "Fechado"),
        ("3", "Pago"),
        ("4", "Saiu para a entrega"),
        ("5", "Entregue"),
    )
    
    vendedor = models.ForeignKey(Vendedor, on_delete=models.CASCADE, verbose_name="Vendedor")
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, verbose_name="Cliente")
    formaPagamento = models.CharField("Forma de pagamento", max_length=1, choices=PAG_CHOICES, blank=False, null=False)
    formaDivulgacao = models.CharField("Forma de divulgação", max_length=1, choices=DIV_CHOICES, blank=False, null=False)
    statusPedido = models.CharField("Status do pedido", max_length=1, choices=STATUS_CHOICES, blank=False, null=False)
    
    dataCriacao = models.DateTimeField('Data de criação', auto_now_add=True)
    dataAtualizacao = models.DateTimeField('Última data de atualização', auto_now=True)

    class Meta:
        verbose_name = 'Venda'
        verbose_name_plural = '5 - Venda'

    def __str__(self):
        return str(self.cliente)
    
class ItensVenda(models.Model):
    venda = models.ForeignKey(Venda, on_delete=models.CASCADE, verbose_name="Venda")
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE, verbose_name="Produto")
    quantidade = models.IntegerField("Quantidade", blank=True,null=True)
    
    dataCriacao = models.DateTimeField('Data de criação', auto_now_add=True)
    dataAtualizacao = models.DateTimeField('Última data de atualização', auto_now=True)

    class Meta:
        verbose_name = 'Itens da Venda'
        verbose_name_plural = '6 - Itens da Venda'

    def __str__(self):
        return str(self.produto)