from django.urls import path

from ecommerce.addresses.views import AddressCreateView, AddressListView

app_name = 'addresses'

urlpatterns = (
    path('create/', AddressCreateView.as_view(), name='create'),
    path('', AddressListView.as_view(), name='list'),
)
