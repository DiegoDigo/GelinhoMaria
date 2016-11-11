from django.conf.urls import url
from . import views
from rest_framework_swagger.views import get_swagger_view

shema_view = get_swagger_view(title="Tipos e sabores gelinhos")

urlpatterns = [
    url(r'^tipos/$', views.ListarTipo.as_view()),
    url(r'^salvar/tipo/$', views.SalvarTipoGelinho.as_view()),
    url(r'^sabores/$', views.ListarSabores.as_view()),
    url(r'^salvar/sabor/$', views.SalvarSaborGelinho.as_view()),
    url(r'^$', shema_view)
]