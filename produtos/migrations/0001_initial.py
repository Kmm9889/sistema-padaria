# Generated by Django 5.1.4 on 2025-01-09 00:00

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Encomenda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_da_pessoa', models.CharField(max_length=100)),
                ('Produto_reservado', models.CharField(max_length=100)),
                ('numero_de_telefone', models.CharField(max_length=15)),
                ('descricao', models.CharField(max_length=200)),
                ('preco', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('estoque', models.IntegerField(default=0)),
                ('endereço_da_entrega', models.CharField(max_length=30)),
                ('Novidade', models.BooleanField(default=False)),
                ('forma_de_pagamento', models.CharField(choices=[('pix', 'Pix'), ('debito', 'Debito'), ('credito', 'Credito'), ('dinheiro', 'Dinheiro')], default='pix', max_length=50)),
                ('data_e_hora_da_compra', models.DateTimeField(default=django.utils.timezone.now)),
                ('foto_do_Produto_Encomendado', models.ImageField(blank=True, null=True, upload_to='media/Encomendas')),
            ],
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_do_produto', models.CharField(max_length=150)),
                ('descricao', models.CharField(max_length=200)),
                ('avaliacao', models.TextField()),
                ('estoque', models.IntegerField()),
                ('preco', models.DecimalField(decimal_places=2, max_digits=10)),
                ('novidade', models.BooleanField()),
                ('foto_do_produto', models.ImageField(blank=True, null=True, upload_to='media/Cardapio')),
            ],
        ),
    ]
