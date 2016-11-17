from django.conf.urls import url
from . import views

urlpatterns =[
    url(r'^vendas/$', views.ListarVendas.as_view())
]