from django.contrib.auth import get_user_model, views as auth_views, mixins as auth_mixins, logout, login
from django.contrib.sites.shortcuts import get_current_site
from django.core.exceptions import ValidationError
from django.template.loader import render_to_string
from django.urls import reverse_lazy, reverse
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.views import generic as views

from ecommerce.accounts.forms import UserRegisterForm, UserPasswordResetForm, ProfileUpdateForm, UserDeactivateUpdateForm
from ecommerce.accounts.tasks import send_account_activation_email
from ecommerce.accounts.tokens import account_activation_token
from ecommerce.common.view_mixins import RedirectAuthenticatedUserMixin

UserModel = get_user_model()


class UserRegisterView(RedirectAuthenticatedUserMixin, views.CreateView):
    form_class = UserRegisterForm
    template_name = 'accounts/registration/user_register.html'
    success_url = reverse_lazy('accounts:user created')

    def form_valid(self, form):
        response = super().form_valid(form=form)
        current_site = get_current_site(self.request)
        message = render_to_string('accounts/registration/user_activation_email.html', {
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(self.object.pk)),
            'token': account_activation_token.make_token(self.object),
        })
        send_account_activation_email.delay(message, self.object.email)
        return response


class UserCreatedView(views.TemplateView):
    template_name = 'accounts/registration/user_created.html'


class UserActivateRedirectView(views.RedirectView):
    @staticmethod
    def get_user(uidb64):
        try:
            uid = urlsafe_base64_decode(uidb64).decode()
            user = UserModel._default_manager.get(pk=uid)
        except (
                TypeError,
                ValueError,
                OverflowError,
                UserModel.DoesNotExist,
                ValidationError,
        ):
            user = None
        return user

    def get_redirect_url(self, uidb64, token):
        user = self.get_user(uidb64)
        if user is not None and account_activation_token.check_token(user, token):
            user.is_active = True
            user.save()
            login(self.request, user)
            return reverse('accounts:user activated')
        else:
            return reverse('accounts:user not activated')


class UserActivatedView(views.TemplateView):
    template_name = 'accounts/registration/user_activated.html'


class UserNotActivatedView(views.TemplateView):
    template_name = 'accounts/registration/user_not_activated.html'


class UserDeactivateUpdateView(auth_mixins.LoginRequiredMixin, views.UpdateView):
    form_class = UserDeactivateUpdateForm
    template_name = 'accounts/deactivation/user_deactivate.html'
    success_url = reverse_lazy('accounts:user deactivate done')

    def get_object(self, queryset=None):
        return self.request.user

    def form_valid(self, form):
        form.instance.is_active = False
        logout(self.request)
        return super().form_valid(form)


class UserDeactivateDoneView(views.TemplateView):
    template_name = 'accounts/deactivation/user_deactivate_done.html'


class UserLoginView(auth_views.LoginView):
    template_name = 'accounts/user_login.html'
    redirect_authenticated_user = True


class UserLogoutView(auth_mixins.LoginRequiredMixin, auth_views.LogoutView):
    pass


class UserDetailView(auth_mixins.LoginRequiredMixin, views.DetailView):
    template_name = 'accounts/user_details.html'
    context_object_name = 'user'

    def get_object(self, queryset=None):
        return self.request.user


class UserPasswordResetView(RedirectAuthenticatedUserMixin, auth_views.PasswordResetView):
    form_class = UserPasswordResetForm
    template_name = 'accounts/password_reset/user_password_reset.html'
    email_template_name = 'accounts/password_reset/user_password_reset_email.html'
    success_url = reverse_lazy('accounts:user password reset done')


class UserPasswordResetDoneView(auth_views.PasswordResetDoneView):
    template_name = 'accounts/password_reset/user_password_reset_done.html'


class UserPasswordResetConfirmView(auth_views.PasswordResetConfirmView):
    template_name = 'accounts/password_reset/user_password_reset_confirm.html'
    success_url = reverse_lazy('accounts:user password reset complete')


class UserPasswordResetCompleteView(auth_views.PasswordResetCompleteView):
    template_name = 'accounts/password_reset/user_password_reset_complete.html'


class UserPasswordChangeView(auth_views.PasswordChangeView):
    template_name = 'accounts/password_change/user_password_change.html'
    success_url = reverse_lazy('accounts:user password change done')


class UserPasswordChangeDoneView(auth_views.PasswordChangeDoneView):
    template_name = 'accounts/password_change/user_password_change_done.html'


class ProfileUpdateView(auth_mixins.LoginRequiredMixin, views.UpdateView):
    form_class = ProfileUpdateForm
    template_name = 'accounts/profile_update.html'
    success_url = reverse_lazy('accounts:user details')

    def get_object(self, queryset=None):
        return self.request.user.profile
