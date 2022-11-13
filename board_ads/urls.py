from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from ads import views
from ads.views import AdsView, AdView, CategoryView, CategoriesView
from board_ads import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('cat/', CategoriesView.as_view()),
    path('ad/', AdsView.as_view()),
    path('cat/<int:pk>', CategoryView.as_view()),
    path('ad/<int:pk>', AdView.as_view()),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)