from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from gelinho.models import TipoGelinho, SaborGelinho
from . import serializers


class ListarTipo(generics.ListAPIView):
    queryset = TipoGelinho.objects.all()
    serializer_class = serializers.SerializerTipoGelinho
    permission_classes = [IsAuthenticated, ]


class SalvarTipoGelinho(generics.CreateAPIView):
    queryset = TipoGelinho.objects.all()
    serializer_class = serializers.SerializerSalvarTipoGelinho
    permission_classes = [IsAuthenticated, ]


class ListarSabores(generics.ListAPIView):
    queryset = SaborGelinho.objects.all()
    serializer_class = serializers.SerializerSaborGelinho
    permission_classes = [IsAuthenticated, ]


class SalvarSaborGelinho(generics.CreateAPIView):
    queryset = SaborGelinho.objects.all()
    serializer_class = serializers.SerializerSalvarSaborGelinho
    permission_classes = [IsAuthenticated, ]