from rest_framework import generics
from vendas.models import Venda
from .serializers import SerializerListarVendas


class ListarVendas(generics.ListAPIView):
    queryset = Venda.objects.all()
    serializer_class = SerializerListarVendas
