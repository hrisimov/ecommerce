from django.urls import path

from ecommerce.addresses.views import AddressCreateView

app_name = 'addresses'

urlpatterns = (
    path('create/', AddressCreateView.as_view(), name='create'),
)
