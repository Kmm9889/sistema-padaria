"""
URL configuration for sistema project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import home, sobre_nos, cardapio, contato, novidades, cadastro, encomenda
from .views import cart_add, cart_remove, cart_update, cart_get, cart_checkout, cadastro_rapido
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', home, name='home'),
    path('home/', home, name='home'),
    path('sobre_nos', sobre_nos, name='sobre_nos'),
    path('cardapio', cardapio, name='cardapio'),
    path('contato', contato , name='contato'),
    path('novidades', novidades, name='novidades'),
    path('encomenda', encomenda, name="encomenda"),
    path('cadastro', cadastro, name='cadastro'),
    path('cadastro_rapido/', cadastro_rapido, name='cadastro_rapido'),
    path('admin/', admin.site.urls),
    path('cart/add/', cart_add, name='cart_add'),
    path('cart/remove/', cart_remove, name='cart_remove'),
    path('cart/update/', cart_update, name='cart_update'),
    path('cart/get/', cart_get, name='cart_get'),
    path('cart/checkout/', cart_checkout, name='cart_checkout'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = 'Administração - Recanto do Pão'
admin.site.index_title = 'Painel de Gestão'
admin.site.site_title = 'Recanto do Pão | Sistema Administrativo'