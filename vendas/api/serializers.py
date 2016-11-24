from rest_framework import serializers
from vendas.models import Venda
from gelinho.api.serializers import SerializerSaborGelinho


class SerializerListarVendas(serializers.ModelSerializer):
    gelinho = SerializerSaborGelinho(read_only=True)

    class Meta:
        model = Venda
        fields = "__all__"

