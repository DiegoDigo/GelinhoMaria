from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^v1/', include('usuarios.urls')),
    url(r'^v1/gelinho/', include('gelinho.api.urls')),
    url(r'^v1/venda/', include('vendas.api.urls'))
]
if settings.DEBUG:
    urlpatterns += static(settings.MIDIA_URL, document_root=settings.MIDIA_ROOT)
