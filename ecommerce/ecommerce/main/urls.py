from django.urls import path

from ecommerce.main.views import DashboardView

app_name = 'main'

urlpatterns = (
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
)
