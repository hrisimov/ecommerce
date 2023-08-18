from django.urls import path

from ecommerce.addresses.views import AddressCreateView, AddressListView, AddressEditView, delete_address, \
    set_new_default_address

app_name = 'addresses'

urlpatterns = (
    path('create/', AddressCreateView.as_view(), name='create'),
    path('', AddressListView.as_view(), name='list'),
    path('edit/<uuid:pk>/', AddressEditView.as_view(), name='edit'),
    path('delete/', delete_address, name='delete'),
    path('set-default/', set_new_default_address, name='set default'),
)
