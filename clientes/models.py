from django.db import models

class Contato(models.Model):
    nome = models.CharField(max_length=150)
    email = models.EmailField()
    avaliação_da_padaria = models.TextField()

    def _str_(self):
        return self.nome

class Vip(models.Model):
    nome = models.CharField(max_length=150)
    email = models.EmailField()
    avaliação_da_padaria = models.TextField()

    def _str_(self):
        return self.nome
