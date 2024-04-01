from django.urls import path

from ecommerce.accounts.views import (
    UserRegisterView,
    UserCreatedView,
    UserActivateRedirectView,
    UserActivatedView,
    UserNotActivatedView,
    UserDeactivateUpdateView,
    UserDeactivateDoneView,
    UserLoginView,
    UserLogoutView,
    UserDetailView,
    UserPasswordResetView,
    UserPasswordResetDoneView,
    UserPasswordResetConfirmView,
    UserPasswordResetCompleteView,
    UserPasswordChangeView,
    UserPasswordChangeDoneView,
    ProfileUpdateView,
)

app_name = 'accounts'

urlpatterns = (
    path('register/', UserRegisterView.as_view(), name='user register'),
    path('created/', UserCreatedView.as_view(), name='user created'),
    path('activate/<uidb64>/<token>/', UserActivateRedirectView.as_view(), name='user activate'),
    path('activated/', UserActivatedView.as_view(), name='user activated'),
    path('not-activated/', UserNotActivatedView.as_view(), name='user not activated'),
    path('deactivate/', UserDeactivateUpdateView.as_view(), name='user deactivate'),
    path('deactivate-done/', UserDeactivateDoneView.as_view(), name='user deactivate done'),
    path('login/', UserLoginView.as_view(), name='user login'),
    path('logout/', UserLogoutView.as_view(), name='user logout'),
    path('details/', UserDetailView.as_view(), name='user details'),
    path('password-reset/', UserPasswordResetView.as_view(), name='user password reset'),
    path('password-reset-done/', UserPasswordResetDoneView.as_view(), name='user password reset done'),
    path('password-reset-confirm/<uidb64>/<token>/', UserPasswordResetConfirmView.as_view(), name='user password reset confirm'),
    path('password-reset-complete/', UserPasswordResetCompleteView.as_view(), name='user password reset complete'),
    path('password-change/', UserPasswordChangeView.as_view(), name='user password change'),
    path('password-change-done/', UserPasswordChangeDoneView.as_view(), name='user password change done'),
    path('update/', ProfileUpdateView.as_view(), name='profile update'),
)
