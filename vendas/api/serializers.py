from rest_framework import  serializers
from vendas.models import Venda


class SerializerListarVendas(serializers.ModelSerializer):
    # sabor = serializers.SerializerMethodField()
    # tipo = serializers.SerializerMethodField()

    class Meta:
        model = Venda
        fields =('sabor', 'tipo', 'qtd_venda', 'valor_venda', 'data_venda' )

    # def get_sabor(self, obj):
    #     return str(obj.sabor.sabor)
    #
    # def get_tipo(self, obj):
    #     return str(obj.tipo.tipo)