from django.db import models
from django.conf import settings
from gelinho.models import TipoGelinho, SaborGelinho


class Venda(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    sabor = models.ForeignKey(SaborGelinho)
    tipo = models.ForeignKey(TipoGelinho)
    qtd_venda = models.IntegerField('Quantidade Vendida')
    valor_venda = models.DecimalField('Valor Total Venda', decimal_places=2,max_digits=5)
    data_venda = models.DateField('Data Venda', auto_now_add=False, auto_now=False)

    def __str__(self):
        return self.usuario.username