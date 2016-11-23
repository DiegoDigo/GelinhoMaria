from rest_framework import serializers
from gelinho.models import TipoGelinho, SaborGelinho


class SerializerTipoGelinho(serializers.ModelSerializer):
    class Meta:
        model = TipoGelinho
        fields = ('id','tipo')


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

    # def get_tipo_gelinho(self, obj):
    #     return str(obj.tipo_gelinho.tipo)
