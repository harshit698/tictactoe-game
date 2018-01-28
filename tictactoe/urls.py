from django.conf.urls import url,include
from django.contrib import admin

from .view import welcome

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^player/',include('player.urls')),
    url(r'^welcome$',welcome),
]
