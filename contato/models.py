from django.db import models

class Contato(models.Model):
    nome = models.CharField(max_length=150)
    email = models.EmailField()
    descricao = models.TextField()

    def _str_(self):
        return self.nome
