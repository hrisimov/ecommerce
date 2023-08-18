from django.contrib.auth import mixins as auth_mixins
from django.views import generic as views

from ecommerce.addresses.forms import AddressCreateForm
from ecommerce.addresses.models import Address


class AddressCreateView(auth_mixins.LoginRequiredMixin, views.CreateView):
    form_class = AddressCreateForm
    template_name = 'addresses/address_create.html'
    # success_url = None

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class AddressListView(auth_mixins.LoginRequiredMixin, views.ListView):
    model = Address
    template_name = 'addresses/addresses_list.html'

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)
