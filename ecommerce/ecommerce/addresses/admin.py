from django.contrib import admin

from ecommerce.addresses.models import Address


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('user', 'province', 'town_city', 'address_line')
