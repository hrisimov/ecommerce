from django.urls import path

from ecommerce.baskets.views import add_product_to_basket

app_name = 'baskets'

urlpatterns = (
    path('add-product/<slug:slug>/', add_product_to_basket, name='add product'),
)
