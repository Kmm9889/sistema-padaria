from django.shortcuts import render
from contato.models import Contato
from produtos.models import Cardapio
from produtos.models import Encomenda

def home(request):
    return render(request, 'home.html')

def sobre_nos(request):
    return render(request, 'sobre_nos.html')

def cadastro(request):
    return render(request, 'cadastro.html')

def cardapio(request):
    todos_os_produtos = Cardapio.objects.all()
    produtos_padaria = {
        "lista_produtos": todos_os_produtos
    }
   
    return render(request, "cardapio.html", produtos_padaria )

def contato(request):
    if request.method == "POST":
        _nome = request.POST.get("nome")
        _email = request.POST.get("email")
        _mensagem = request.POST.get("mensagem")
        contato = Contato(nome=_nome, email=_email, mensagem=_mensagem)
        contato.save()
        dados = {
            "mensagem": "Sua mensagem foi enviada com sucesso!"
        }
        return render(request, "Contato.html", dados)

    else:
        return render(request, "Contato.html")

def encomenda(request):
    if request.method == "POST":
        _nome_da_pessoa = request.POST.get("nome_da_pessoa")
        _numero_de_telefone = request.POST.get("numero_de_telefone")
        _Produto_reservado = request.POST.get("Produto_reservado")
        _endereço_da_entrega = request.POST.get("endereço_da_entrega")
        _forma_de_pagamento = request.POST.get("forma_de_pagamento")
        encomenda = Encomenda(forma_de_pagamento=_forma_de_pagamento, nome_da_pessoa=_nome_da_pessoa, numero_de_telefone=_numero_de_telefone, endereço_da_entrega=_endereço_da_entrega, Produto_reservado=_Produto_reservado, )
        encomenda.save()
        dados = {
            "mensagem": "Sua encomenda foi feita com sucesso!"
        }
        return render(request, "encomenda.html", dados)

    else:
        return render(request, "encomenda.html")

def novidades(request):
    return render(request, 'novidades.html')

