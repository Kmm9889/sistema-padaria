from django.db import models

class Cardapio(models.Model):
    nome_do_produto = models.CharField(max_length=150)
    descricao = models.CharField(max_length=200)
    avaliação = models.TextField()
    estoque = models.IntegerField()
    preco = models.DecimalField(decimal_places=2, max_digits=10)
    Novidade = models.BooleanField()
    foto_do_produto = models.ImageField(upload_to='Vendas', blank=True, null=True)

    def _str_(self):
        return self.nome_do_produto
    
class Encomenda(models.Model):
    Produto_reservado = models.CharField(max_length=100)
    descricao = models.CharField(max_length=200)
    preco = models.DecimalField(decimal_places=2, max_digits=10)
    estoque = models.IntegerField()
    endereço_da_entrega = models.CharField(max_length=30)
    Novidade = models.BooleanField()
    data_da_e_hora_da_compra = models.DateTimeField()
    foto_do_Produto_Encomendado = models.ImageField(upload_to='Encomenda', blank=True, null=True)

    def _str_(self):
        return self.Produto_reservado
