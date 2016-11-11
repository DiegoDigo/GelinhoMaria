from rest_framework import serializers
from gelinho.models import TipoGelinho , SaborGelinho


class SerializerTipoGelinho(serializers.ModelSerializer):
    class Meta:
        model = TipoGelinho
        fields = '__all__'


class SerializerSalvarTipoGelinho(serializers.ModelSerializer):
    class Meta:
        model = TipoGelinho
        fields = ['tipo', ]


class SerializerSalvarSaborGelinho(serializers.ModelSerializer):

    class Meta:
        model = SaborGelinho
        fields = ['sabor', 'tipo_gelinho', 'qtd', 'valor_uni', 'valor_total', ]


class SerializerSaborGelinho(serializers.ModelSerializer):
    tipo_gelinho = serializers.SerializerMethodField()

    class Meta:
        model = SaborGelinho
        fields = '__all__'

    def get_tipo_gelinho(self, obj):
        return str(obj.tipo_gelinho.tipo)


