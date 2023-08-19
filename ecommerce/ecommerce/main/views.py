from django.contrib.auth import mixins as auth_mixins
from django.views import generic as views


class DashboardView(auth_mixins.LoginRequiredMixin, views.TemplateView):
    template_name = 'main/dashboard.html'
