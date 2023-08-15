from django.urls import path

from ecommerce.baskets.views import add_product_to_basket, get_basket_summary

app_name = 'baskets'

urlpatterns = (
    path('add-product/<slug:slug>/', add_product_to_basket, name='add product'),
    path('summary/', get_basket_summary, name='summary'),
)
