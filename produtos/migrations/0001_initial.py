# Generated by Django 5.1.4 on 2024-12-07 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cardapio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_do_produto', models.CharField(max_length=150)),
                ('descricao', models.CharField(max_length=200)),
                ('avaliação', models.TextField()),
                ('estoque', models.IntegerField()),
                ('preco', models.DecimalField(decimal_places=2, max_digits=10)),
                ('disponibilidade', models.BooleanField()),
                ('foto_do_produto', models.ImageField(blank=True, null=True, upload_to='Vendas')),
            ],
        ),
        migrations.CreateModel(
            name='Encomenda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Produto_reservado', models.CharField(max_length=100)),
                ('descricao', models.CharField(max_length=200)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=10)),
                ('estoque', models.IntegerField()),
                ('endereço_da_entrega', models.CharField(max_length=30)),
                ('disponibilidade', models.BooleanField()),
                ('data_da_e_hora_da_compra', models.DateTimeField()),
                ('foto_do_Produto_Encomendado', models.ImageField(blank=True, null=True, upload_to='Encomenda')),
            ],
        ),
    ]
