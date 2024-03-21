from django.http import HttpResponseRedirect
from django.urls import reverse_lazy


class RedirectAuthenticatedUserMixin:
    redirect_url = reverse_lazy('main:dashboard')

    def get_redirect_url(self):
        return str(self.redirect_url)

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_redirect_url())
        return super().dispatch(request, *args, **kwargs)
