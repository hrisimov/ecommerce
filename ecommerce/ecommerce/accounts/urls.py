from django.urls import path

from ecommerce.accounts.views import register, activate

urlpatterns = (
    path('register/', register, name='register'),
    path('activate/<uidb64>/<token>/', activate, name='activate'),
)

from . import signals
