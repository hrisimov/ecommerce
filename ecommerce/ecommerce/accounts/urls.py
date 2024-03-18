from django.urls import path

from ecommerce.accounts.views import UserRegisterView, activate_user, UserLoginView, UserLogoutView, UserPasswordResetView, \
    UserPasswordResetDoneView, UserPasswordResetConfirmView, UserPasswordResetCompleteView, get_account_details, \
    UserPasswordChangeView, UserPasswordChangeDoneView, edit_account, delete_account, AccountDeleteDoneView, \
    UserCreatedView, UserActivatedView, UserNotActivatedView

app_name = 'accounts'

urlpatterns = (
    path('register/', UserRegisterView.as_view(), name='user register'),
    path('created/', UserCreatedView.as_view(), name='user created'),
    path('activate/<uidb64>/<token>/', activate_user, name='user activate'),
    path('activated/', UserActivatedView.as_view(), name='user activated'),
    path('not-activated/', UserNotActivatedView.as_view(), name='user not activated'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('password-reset/', UserPasswordResetView.as_view(), name='password reset'),
    path('password-reset-done/', UserPasswordResetDoneView.as_view(), name='password reset done'),
    path('password-reset-confirm/<uidb64>/<token>/', UserPasswordResetConfirmView.as_view(), name='password reset confirm'),
    path('password-reset-complete/', UserPasswordResetCompleteView.as_view(), name='password reset complete'),
    path('details/', get_account_details, name='details'),
    path('password-change/', UserPasswordChangeView.as_view(), name='password change'),
    path('password-change-done/', UserPasswordChangeDoneView.as_view(), name='password change done'),
    path('edit/', edit_account, name='edit'),
    path('delete/', delete_account, name='delete'),
    path('delete-done/', AccountDeleteDoneView.as_view(), name='delete done'),
)
