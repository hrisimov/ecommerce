from django import forms

from ecommerce.addresses.models import Address


class AddressBaseForm(forms.ModelForm):
    class Meta:
        model = Address
        exclude = ('id', 'default', 'user')


class AddressCreateForm(AddressBaseForm):
    class Meta(AddressBaseForm.Meta):
        pass


class AddressEditForm(AddressBaseForm):
    class Meta(AddressBaseForm.Meta):
        pass
