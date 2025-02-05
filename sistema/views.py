from django.shortcuts import render
from contato.models import Contato
from produtos.models import Produto
from produtos.models import Encomenda
from clientes.models import Cliente

def home(request):
    return render(request, 'home.html')

def sobre_nos(request):
    return render(request, 'sobre_nos.html')

def cadastro(request):
    if request.method == 'POST':
        _nome = request.POST.get('nome')
        _email = request.POST.get('email')
        _numero_de_telefone = request.POST.get('numero_de_telefone')
        _endereco = request.POST.get('endereco')
        _foto_do_cliente = request.FILES.get('foto_do_cliente')
        cliente = Cliente(nome=_nome, email=_email, numero_de_telefone=_numero_de_telefone, endereco=_endereco, foto_do_cliente=_foto_do_cliente)
        cliente.save()
        
        dados = {
            "mensagem": "Você foi cadastrado com sucesso!"
        }
        return render(request, 'cadastro.html', dados)
    else:
        return render(request, 'cadastro.html')
     
def cardapio(request):
    todos_os_produtos = Produto.objects.all()
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
        _produtos_encomendados = request.POST.get("produtos_encomendados")
        _endereço_da_entrega = request.POST.get("endereço_da_entrega")
        _forma_de_pagamento = request.POST.get("forma_de_pagamento")
        encomenda = Encomenda(forma_de_pagamento=_forma_de_pagamento, nome_da_pessoa=_nome_da_pessoa, numero_de_telefone=_numero_de_telefone, endereço_da_entrega=_endereço_da_entrega, produtos_encomendados=_produtos_encomendados, )
        encomenda.save()
        dados = {
            "mensagem": "Sua encomenda foi feita com sucesso!"
        }
        return render(request, "encomenda.html", dados)

    else:
        return render(request, "encomenda.html")

def novidades(request):
    produtos_novidades = Produto.objects.filter(novidade=True)
    novidades_lista = {
        "lista_produtos": produtos_novidades
    }
    return render(request, 'novidades.html', novidades_lista)

