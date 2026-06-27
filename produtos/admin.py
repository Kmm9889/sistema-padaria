import re
from django.contrib import admin
from .models import Produto, Encomenda


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = (
        'nome_do_produto',
        'descricao',
        'estoque',
        'preco',
        'desconto',
        'preco_com_desconto',
        'novidade',
    )
    
    list_editable = (
        'estoque',
        'preco',
        'desconto',
        'novidade',
    )
    
    search_fields = (
        'nome_do_produto',
        'descricao',
    )
    
    list_filter = (
        'novidade',
        'estoque',
    )
    
    ordering = (
        'nome_do_produto',
        'estoque',
    )


@admin.register(Encomenda)
class EncomendaAdmin(admin.ModelAdmin):
    list_display = (
        'nome_da_pessoa',
        'produtos_encomendados',
        'numero_de_telefone',
        'total',
        'forma_de_pagamento',
        'data_e_hora_da_compra',
        'data_e_hora_da_entrega',
    )
    
    actions = ['extornar_encomenda']
    
    search_fields = (
        'nome_da_pessoa',
        'produtos_encomendados',
        'numero_de_telefone',
    )
    
    list_filter = (
        'forma_de_pagamento',
        'data_e_hora_da_compra',
        'data_e_hora_da_entrega',
    )
    
    date_hierarchy = 'data_e_hora_da_compra'
    
    ordering = (
        '-data_e_hora_da_compra',
    )

    def extornar_encomenda(self, request, queryset):
        count = 0
        for encomenda in queryset:
            for linha in encomenda.produtos_encomendados.split('\n'):
                match = re.match(r'(.+?)\s*x(\d+)\s*-\s*R\$', linha.strip())
                if match:
                    nome = match.group(1).strip()
                    qtd = int(match.group(2))
                    try:
                        produto = Produto.objects.get(nome_do_produto=nome)
                        produto.estoque += qtd
                        produto.save()
                        count += 1
                    except Produto.DoesNotExist:
                        pass
        self.message_user(request, f'{count} produto(s) devolvido(s) ao estoque de {queryset.count()} encomenda(s).')
    extornar_encomenda.short_description = 'Extornar encomendas selecionadas (devolver ao estoque)'