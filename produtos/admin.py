
from django.contrib import admin
from .models import Produto
from .models import Encomenda

admin.site.register(Produto)
admin.site.register(Encomenda)
