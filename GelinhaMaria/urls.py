from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^user/', include('rest_auth.urls')),
    url(r'^v1/', include('gelinho.api.urls'))
]
