from django.urls import path

from ecommerce.products.views import ProductsListView, ProductDetailView

app_name = 'products'

urlpatterns = (
    path('', ProductsListView.as_view(), name='list'),
    path('category/<slug:slug>/', ProductsListView.as_view(), name='list by category'),
    path('<slug:slug>/', ProductDetailView.as_view(), name='product details'),
)
