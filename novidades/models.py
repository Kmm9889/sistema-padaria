from django.db import models

class Novidade(models.Model):
    nome_do_produto = models.CharField(max_length=150)
    descricao = models.CharField(max_length=200)
    avaliação_dos_Chefs = models.TextField()
    preco = models.DecimalField(decimal_places=2, max_digits=10)
    foto_do_produto = models.ImageField(upload_to='Novidades', blank=True, null=True)

    def _str_(self):
        return self.nome_do_produto
