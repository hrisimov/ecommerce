from django.urls import path

from ecommerce.products.views import ProductsListView

app_name = 'products'

urlpatterns = (
    path('', ProductsListView.as_view(), name='list'),
    path('category/<slug:slug>/', ProductsListView.as_view(), name='list by category'),
)
