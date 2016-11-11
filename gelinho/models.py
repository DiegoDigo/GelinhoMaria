from django.db import models


class TipoGelinho(models.Model):
    tipo = models.CharField('Tipo', max_length=100, unique=True)

    def __str__(self):
        return self.tipo

    class Meta:
        ordering = ['tipo']
        verbose_name = 'TipoGelinho'
        verbose_name_plural = 'TiposGelinho'


class SaborGelinho(models.Model):
    sabor = models.CharField('Sabor', max_length=100)
    tipo_gelinho = models.ForeignKey(TipoGelinho)
    qtd = models.IntegerField('Quatidade')
    valor_uni = models.DecimalField('Valor Unitario', max_digits=5, decimal_places=2)
    valor_total = models.DecimalField('Valor Total', max_digits=5, decimal_places=2)

    def __str__(self):
        return self.sabor

    class Meta:
        ordering = ['sabor']
        verbose_name ='SaborGelinho'
        verbose_name_plural ='SaboresGelinhos'
        default_related_name = 'Tipos'