from django.contrib import admin
from django.urls import path
from products.views import (dynamic_lookup_view, product_create_view,
                            product_delete_view, product_detail_view,
                            product_list_view)

app_name = 'products'
urlpatterns = [
    path('', product_list_view, name="products"),
    path('<int:id>/', dynamic_lookup_view, name="product-details"),
    path('<int:id>/delete', product_delete_view, name="product-delete"),
    path('create/', product_create_view),
]
