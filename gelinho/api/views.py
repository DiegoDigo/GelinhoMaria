from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from gelinho.models import TipoGelinho, SaborGelinho
from . import serializers


class ListarTipo(ListAPIView):
    queryset = TipoGelinho.objects.all()
    serializer_class = serializers.SerializerTipoGelinho
    permission_classes = [IsAuthenticated, ]


class ListarSabores(ListAPIView):
    queryset = SaborGelinho.objects.all()
    serializer_class = serializers.SerializerSaborGelinho
    permission_classes = [IsAuthenticated, ]