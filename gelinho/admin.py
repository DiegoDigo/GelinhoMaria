from django.contrib import admin
from .models import TipoGelinho, SaborGelinho


class AdminTipoGelinho(admin.ModelAdmin):
    list_display = ['tipo']
    ordering = ['tipo']


class AdminSaborGelinho(admin.ModelAdmin):
    list_display = ['sabor', 'tipo_gelinho', 'qtd', 'valor_uni']
    ordering = ['sabor']

admin.site.register(TipoGelinho, AdminTipoGelinho)
admin.site.register(SaborGelinho, AdminSaborGelinho)