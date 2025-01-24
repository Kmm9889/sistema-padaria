from django.contrib import admin
from .models import Produto, Encomenda


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = (
        'nome_do_produto',
        'descricao',
        'estoque',
        'preco',
        'novidade',
    )
    
    search_fields = (
        'nome_do_produto',
        'descricao',
    )
    
    list_filter = (
        'novidade',
    )
    
    ordering = (
        'nome_do_produto',
        'estoque',
    )


@admin.register(Encomenda)
class EncomendaAdmin(admin.ModelAdmin):
    list_display = (
        'nome_da_pessoa',
        'Produto_reservado',
        'numero_de_telefone',
        'total',
        'forma_de_pagamento',
        'data_e_hora_da_compra',
        'data_e_hora_da_encomenda',
    )
    
    search_fields = (
        'nome_da_pessoa',
        'Produto_reservado',
        'numero_de_telefone',
    )
    
    list_filter = (
        'forma_de_pagamento',
        'data_e_hora_da_compra',
        'data_e_hora_da_encomenda',
    )
    
    date_hierarchy = 'data_e_hora_da_compra'
    
    ordering = (
        '-data_e_hora_da_compra',
    )