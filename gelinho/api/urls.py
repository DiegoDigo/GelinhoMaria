from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^tipos/$', views.ListarTipo.as_view()),
    url(r'^sabores/$', views.ListarSabores.as_view())
]