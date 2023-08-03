from django.urls import path

from ecommerce.accounts.views import register, activate, UserLoginView, UserLogoutView, UserPasswordResetView, \
    UserPasswordResetDoneView, UserPasswordResetConfirmView, UserPasswordResetCompleteView

app_name = 'accounts'

urlpatterns = (
    path('register/', register, name='register'),
    path('activate/<uidb64>/<token>/', activate, name='activate'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('password-reset/', UserPasswordResetView.as_view(), name='password reset'),
    path('password-reset-done/', UserPasswordResetDoneView.as_view(), name='password reset done'),
    path('password-reset-confirm/<uidb64>/<token>/', UserPasswordResetConfirmView.as_view(), name='password reset confirm'),
    path('password-reset-complete/', UserPasswordResetCompleteView.as_view(), name='password reset complete'),
)

from . import signals
