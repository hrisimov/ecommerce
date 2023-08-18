from django.urls import path

from ecommerce.addresses.views import AddressCreateView, AddressListView, AddressEditView

app_name = 'addresses'

urlpatterns = (
    path('create/', AddressCreateView.as_view(), name='create'),
    path('', AddressListView.as_view(), name='list'),
    path('edit/<uuid:pk>/', AddressEditView.as_view(), name='edit'),
)
