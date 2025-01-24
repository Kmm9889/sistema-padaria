from django.contrib import admin
from .models import Cliente, CartaoFidelidate


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = (
        'nome',
        'email',
        'numero_de_telefone',
        'foto_do_cliente',
        'endereco',
    )
    
    search_fields = (
        'nome',
        'email',
        'numero_de_telefone',
    )
    
    ordering = ('nome',)


@admin.register(CartaoFidelidate)
class CartaoFidelidateAdmin(admin.ModelAdmin): 
    list_display = (
        'cliente',
        'data_visita',
    )
    
    search_fields = (
        'cliente__nome',
        'cliente__email',
    )
    
    ordering = ('-data_visita',)
    
    date_hierarchy = 'data_visita'
    
    list_filter = (
        'data_visita',
    )