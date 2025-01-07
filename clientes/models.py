from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=150)
    email = models.EmailField()
    foto_do_cliente = models.ImageField(upload_to='media/Clientes', blank=True, null=True)
    endereco = models.CharField(max_length=200)

    def __str__(self):
        return self.nome

class CartaoFidelidate(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    data_visita = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.cliente} - {self.data_visita}"
