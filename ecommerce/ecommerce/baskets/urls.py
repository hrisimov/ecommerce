from django.urls import path

from ecommerce.baskets.views import add_product_to_basket, get_basket_summary, update_product_in_basket, \
    delete_product_from_basket

app_name = 'baskets'

urlpatterns = (
    path('add-product/<slug:slug>/', add_product_to_basket, name='add product'),
    path('summary/', get_basket_summary, name='summary'),
    path('update-product/', update_product_in_basket, name='update product'),
    path('delete-product/', delete_product_from_basket, name='delete product'),
)
