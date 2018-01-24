
from django.conf.urls import url
from django.contrib import admin

from .view import welcome

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^welcome$',welcome),
]
