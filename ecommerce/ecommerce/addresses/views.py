import json

from django.contrib.auth import mixins as auth_mixins
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views import generic as views

from ecommerce.addresses.forms import AddressCreateForm, AddressEditForm
from ecommerce.addresses.models import Address


class AddressCreateView(auth_mixins.LoginRequiredMixin, views.CreateView):
    form_class = AddressCreateForm
    template_name = 'addresses/address_create.html'
    success_url = reverse_lazy('addresses:list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class AddressListView(auth_mixins.LoginRequiredMixin, views.ListView):
    model = Address
    template_name = 'addresses/addresses_list.html'

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)


class AddressEditView(auth_mixins.LoginRequiredMixin, views.UpdateView):
    model = Address
    form_class = AddressEditForm
    template_name = 'addresses/address_update.html'
    success_url = reverse_lazy('addresses:list')

    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        if obj not in self.request.user.address_set.all():
            return self.handle_no_permission()
        return obj


@login_required
def delete_address(request):
    if request.method == 'POST':
        body = json.loads(request.body)
        pk = body['addressId']
        address = get_object_or_404(Address, pk=pk)
        address.delete()
        return JsonResponse({
            'message': 'The address was successfully deleted.',
        })


@login_required
def set_new_default_address(request):
    if request.method == 'POST':
        body = json.loads(request.body)
        address_pk = body.get('addressId')
        new_address_pk = body.get('newAddressId')

        if address_pk:
            address = get_object_or_404(Address, pk=address_pk)
            address.default = False
            address.save()

        new_address = get_object_or_404(Address, pk=new_address_pk)
        new_address.default = True
        new_address.save()

        return JsonResponse({
            'message': 'The default address was changed successfully.',
        })
