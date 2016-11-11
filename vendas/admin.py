from django.contrib import admin
from .models import Venda


class AdminVendas(admin.ModelAdmin):
    list_display = ['usuario', 'sabor', 'tipo', 'data_venda', 'qtd_venda', 'valor_venda']
    ordering = ['data_venda', 'sabor']

admin.site.register(Venda, AdminVendas)

