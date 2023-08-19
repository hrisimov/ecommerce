from django.urls import path, reverse_lazy
from django.views.generic import RedirectView

from ecommerce.main.views import DashboardView

app_name = 'main'

urlpatterns = (
    path('', RedirectView.as_view(url=reverse_lazy('products:list'))),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
)
