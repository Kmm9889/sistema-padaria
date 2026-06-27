import json
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_POST
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

@require_POST
def cadastro_rapido(request):
    data = json.loads(request.body)
    cliente = Cliente(
        nome=data.get('nome', ''),
        email=data.get('email', ''),
        numero_de_telefone=data.get('telefone', ''),
        rua=data.get('rua', ''),
        bairro=data.get('bairro', ''),
        endereco=f"{data.get('rua', '')}, {data.get('bairro', '')}",
    )
    cliente.save()
    return JsonResponse({'status': 'ok', 'message': 'Cadastro realizado com sucesso!'})

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
    # Preenche o textarea com os itens do carrinho da sessao
    produtos_texto = None
    cart = request.session.get('cart', {'items': {}})
    if cart.get('items'):
        linhas = []
        for pid, qty in cart['items'].items():
            try:
                produto = Produto.objects.get(id=pid)
                linhas.append(f"{produto.nome_do_produto} x{qty} - R$ {float(produto.preco) * qty:.2f}")
            except Produto.DoesNotExist:
                pass
        if linhas:
            produtos_texto = '\n'.join(linhas)

    if request.method == "POST":
        _nome_da_pessoa = request.POST.get("nome_da_pessoa")
        _numero_de_telefone = request.POST.get("numero_de_telefone")
        _produtos_encomendados = request.POST.get("produtos_encomendados")
        _endereço_da_entrega = request.POST.get("endereço_da_entrega")
        _forma_de_pagamento = request.POST.get("forma_de_pagamento")
        encomenda = Encomenda(forma_de_pagamento=_forma_de_pagamento, nome_da_pessoa=_nome_da_pessoa, numero_de_telefone=_numero_de_telefone, endereço_da_entrega=_endereço_da_entrega, produtos_encomendados=_produtos_encomendados, )
        encomenda.save()
        # Abaixa o estoque dos produtos do carrinho
        cart = request.session.get('cart', {'items': {}})
        if cart.get('items'):
            for pid, qty in cart['items'].items():
                try:
                    produto = Produto.objects.get(id=pid)
                    if produto.estoque >= qty:
                        produto.estoque -= qty
                        produto.save()
                except Produto.DoesNotExist:
                    pass
        # Limpa o carrinho da sessao apos encomendar
        request.session['cart'] = {'items': {}}
        dados = {
            "mensagem": "Sua encomenda foi feita com sucesso!"
        }
        return render(request, "encomenda.html", dados)

    else:
        return render(request, "encomenda.html", {'produtos_texto': produtos_texto})

def novidades(request):
    produtos_novidades = Produto.objects.filter(novidade=True)
    novidades_lista = {
        "lista_produtos": produtos_novidades
    }
    return render(request, 'novidades.html', novidades_lista)

@require_POST
def cart_add(request):
    data = json.loads(request.body)
    product_id = str(data['product_id'])
    quantity = data.get('quantity', 1)

    cart = request.session.get('cart', {})
    items = cart.get('items', {})

    if product_id in items:
        items[product_id] += quantity
    else:
        items[product_id] = quantity

    cart['items'] = items
    request.session['cart'] = cart
    return JsonResponse({'status': 'ok'})

@require_POST
def cart_remove(request):
    data = json.loads(request.body)
    product_id = str(data['product_id'])

    cart = request.session.get('cart', {})
    items = cart.get('items', {})

    items.pop(product_id, None)
    cart['items'] = items
    request.session['cart'] = cart
    return JsonResponse({'status': 'ok'})

@require_POST
def cart_update(request):
    data = json.loads(request.body)
    product_id = str(data['product_id'])
    quantity = data['quantity']

    cart = request.session.get('cart', {})
    items = cart.get('items', {})

    if quantity <= 0:
        items.pop(product_id, None)
    else:
        items[product_id] = quantity

    cart['items'] = items
    request.session['cart'] = cart
    return JsonResponse({'status': 'ok'})

def cart_get(request):
    cart = request.session.get('cart', {'items': {}})
    items_data = {}
    total = 0

    for pid, qty in cart.get('items', {}).items():
        try:
            produto = Produto.objects.get(id=pid)
            subtotal = round(float(produto.preco) * qty, 2)
            total += subtotal
            items_data[pid] = {
                'id': pid,
                'name': produto.nome_do_produto,
                'price': str(produto.preco),
                'quantity': qty,
                'subtotal': str(subtotal),
                'foto': produto.foto_do_produto.url if produto.foto_do_produto else ''
            }
        except Produto.DoesNotExist:
            pass

    return JsonResponse({'items': items_data, 'total': f'{total:.2f}'})

@require_POST
def cart_checkout(request):
    data = json.loads(request.body)
    cart = request.session.get('cart', {'items': {}})

    if not cart['items']:
        return JsonResponse({'status': 'error', 'message': 'Carrinho vazio'})

    produtos_list = []
    total = 0
    for pid, qty in cart['items'].items():
        try:
            produto = Produto.objects.get(id=pid)
            if produto.estoque < qty:
                return JsonResponse({'status': 'error', 'message': f'Estoque insuficiente para {produto.nome_do_produto}'})
            total += float(produto.preco) * qty
            produtos_list.append(f"{produto.nome_do_produto} x{qty} - R$ {float(produto.preco) * qty:.2f}")
        except Produto.DoesNotExist:
            pass

    encomenda = Encomenda(
        nome_da_pessoa=data.get('nome', ''),
        numero_de_telefone=data.get('telefone', ''),
        endereço_da_entrega=data.get('endereco', ''),
        forma_de_pagamento=data.get('pagamento', 'pix'),
        produtos_encomendados='\n'.join(produtos_list),
        total=total,
    )
    encomenda.save()

    # Abaixa o estoque
    for pid, qty in cart['items'].items():
        try:
            produto = Produto.objects.get(id=pid)
            produto.estoque -= qty
            produto.save()
        except Produto.DoesNotExist:
            pass

    request.session['cart'] = {'items': {}}

    return JsonResponse({'status': 'ok', 'message': 'Pedido realizado com sucesso!'})

