from rest_framework import serializers
from gelinho.models import TipoGelinho, SaborGelinho


class SerializerTipoGelinho(serializers.ModelSerializer):
    class Meta:
        model = TipoGelinho
        fields = "__all__"


class SerializerSalvarTipoGelinho(serializers.ModelSerializer):
    class Meta:
        model = TipoGelinho
        fields = ['tipo', ]


class SerializerSalvarSaborGelinho(serializers.ModelSerializer):
    class Meta:
        model = SaborGelinho
        fields = ['sabor', 'tipo_gelinho', 'qtd', 'valor_uni', ]


class SerializerSaborGelinho(serializers.ModelSerializer):
    tipoGelinho = SerializerTipoGelinho(read_only=True)

    class Meta:
        model = SaborGelinho
        fields = ['id', 'sabor', 'tipoGelinho', 'qtd', 'valor_uni', ]