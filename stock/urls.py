from django.urls import path

from .views import product_add, product_list

app_name = 'stock'

urlpatterns = [
    path('', product_list, name='product_list'),
    path('cadastrar', product_add, name='product_add')
]
