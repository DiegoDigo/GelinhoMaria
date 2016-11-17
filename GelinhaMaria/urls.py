from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^v1/', include('usuarios.urls')),
    url(r'^v1/gelinho/', include('gelinho.api.urls')),
    url(r'^v1/venda/', include('vendas.api.urls'))
]
