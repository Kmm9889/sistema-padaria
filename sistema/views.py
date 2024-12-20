from django.shortcuts import render
from contato.models import Contato

def home(request):
    return render(request, 'home.html')

def sobre_nos(request):
    return render(request, 'sobre_nos.html')

def cadastro(request):
    return render(request, 'cadastro.html')

def cardapio(request):
    return render(request, 'cardapio.html')

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

def novidades(request):
    return render(request, 'novidades.html')

