
from django.urls import path
from .views import index, catalog, add_good, ajax_handler

urlpatterns = [
    path('', index),
    path('new', add_good, name='new_good'),
    path('catalog/', catalog),
    path('ajax_handler', ajax_handler, name='ajax_handler')
]