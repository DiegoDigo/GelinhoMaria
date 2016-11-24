from django.contrib import admin
from .models import Venda


class AdminVendas(admin.ModelAdmin):
    list_display = ['gelinho', 'data_venda', 'qtd_venda', 'valor_venda']
    ordering = ['data_venda']

admin.site.register(Venda, AdminVendas)

