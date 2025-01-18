
from django.contrib import admin
from .models import Produto
from .models import Encomenda


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    # Which fields to show in the list (grid) view
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
        'estoque'
    )


@admin.register(Encomenda)
class EncomendaAdmin(admin.ModelAdmin):
    # Fields to display in the list/grid
    list_display = (
        'nome_da_pessoa',
        'Produto_reservado',
        'numero_de_telefone',
        'total',
        'forma_de_pagamento',
        'data_e_hora_da_compra',
        'data_e_hora_da_encomenda',
    )
    
    # Which fields to include in searches
    search_fields = (
        'nome_da_pessoa',
        'Produto_reservado',
        'numero_de_telefone',
    )
    
    # Add filters for easier navigation in the admin
    list_filter = (
        'forma_de_pagamento',
        'data_e_hora_da_compra',
        'data_e_hora_da_encomenda',
    )
    
    # Optional: show a date-based drill-down navigation by 'data_e_hora_da_compra'
    date_hierarchy = 'data_e_hora_da_compra'
    
    # How the admin orders the records by default
    ordering = (
        '-data_e_hora_da_compra',
    )