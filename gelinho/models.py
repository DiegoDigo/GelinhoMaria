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
    tipoGelinho = models.ForeignKey(TipoGelinho, related_name='tipo_gelinho')
    qtd = models.IntegerField('Quatidade')
    valor_uni = models.DecimalField('Valor Unitario', max_digits=5, decimal_places=2)
    imagen = models.ImageField(upload_to='files')

    def __str__(self):
        return self.sabor

    class Meta:
        ordering = ['sabor']
        verbose_name ='SaborGelinho'
        verbose_name_plural ='SaboresGelinhos'
