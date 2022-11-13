from django.urls import path

from ads.views.category import *

urlpatterns = [
    path('', CategoriesView.as_view()),
    path('<int:pk>', CategoryView.as_view()),
]