from rest_framework import serializers
from gelinho.models import TipoGelinho, SaborGelinho


class BaseTipoSabores(serializers.ModelSerializer):
    class Meta:
        model = TipoGelinho
        fields = "__all__"

class BaseSabores(serializers.ModelSerializer):
    class Meta:
        model = SaborGelinho
        fields = "__all__"

class SerializerTipoGelinho(BaseTipoSabores):
    pass

class SerializerSalvarTipoGelinho(serializers.ModelSerializer):
    class Meta:
        model = TipoGelinho
        fields = ['tipo', ]


class SerializerSalvarSaborGelinho(serializers.ModelSerializer):
    class Meta:
        model = SaborGelinho
        fields = ['sabor', 'tipo_gelinho', 'qtd', 'valor_uni', ]


class SerializerSaborGelinho(BaseSabores):
    tipoGelinho = SerializerTipoGelinho(read_only=True)
