from django.contrib.auth import mixins as auth_mixins
from django.views import generic as views

from ecommerce.addresses.forms import AddressCreateForm


class AddressCreateView(auth_mixins.LoginRequiredMixin, views.CreateView):
    form_class = AddressCreateForm
    template_name = 'addresses/address_create.html'
    # success_url = None

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
