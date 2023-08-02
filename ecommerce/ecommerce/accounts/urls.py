from django.urls import path

from ecommerce.accounts.views import register, activate, UserLoginView, UserLogoutView

app_name = 'accounts'

urlpatterns = (
    path('register/', register, name='register'),
    path('activate/<uidb64>/<token>/', activate, name='activate'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
)

from . import signals
