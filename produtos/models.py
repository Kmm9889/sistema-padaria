from django.db import models
from django.utils.timezone import now

class Produto(models.Model):
    nome_do_produto = models.CharField(max_length=150)
    descricao = models.CharField(max_length=3000)
    estoque = models.IntegerField()
    preco = models.DecimalField(decimal_places=2, max_digits=10)
    novidade = models.BooleanField()
    foto_do_produto = models.ImageField(upload_to='Cardapio', blank=True, null=True)

    def __str__(self):
        return self.nome_do_produto
    
class Encomenda(models.Model):
    nome_da_pessoa = models.CharField(max_length=100)
    Produto_reservado = models.CharField(max_length=100)
    numero_de_telefone = models.CharField(max_length=15)
    total = models.DecimalField(decimal_places=2, max_digits=10, default=0)
    endereço_da_entrega = models.CharField(max_length=100)
    forma_de_pagamento = models.CharField(max_length=50, choices=[
        ('cartao', 'Cartao'),
        ('pix', 'Pix'),
        ('dinheiro', 'Dinheiro'),
    ],
    default='pix')
    data_e_hora_da_compra = models.DateTimeField(default=now)
    data_e_hora_da_encomenda = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.nome_da_pessoa
