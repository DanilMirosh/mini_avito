from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from ads.views.index import index
from board_ads import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('ad/', include('ads.urls.ad')),
    path('cat/', include('ads.urls.category'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)