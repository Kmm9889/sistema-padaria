from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=150)
    email = models.EmailField()
    avaliação_da_padaria = models.TextField()
    Cartão_Fidelidade = models.BooleanField()
    foto_do_cliente = models.ImageField(upload_to='media/Clientes', blank=True, null=True)


    def __str__(self):
        return self.nome
