from django.contrib.auth import get_user_model, views as auth_views, logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.views import generic as views

from .forms import UserRegisterForm, UserPasswordResetForm, UserEditForm, ProfileEditForm, UserDeleteForm
from .models import Profile
from .tasks import send_account_activation_email
from .tokens import account_activation_token

UserModel = get_user_model()


class UserRegisterView(views.CreateView):
    form_class = UserRegisterForm
    template_name = 'accounts/registration/user_register.html'
    success_url = reverse_lazy('accounts:user created')

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('main:dashboard')
        return super().dispatch(request, *args, **kwargs)

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


def activate_user(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = UserModel.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, UserModel.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return redirect('accounts:user activated')
    else:
        return redirect('accounts:user not activated')


class UserActivatedView(views.TemplateView):
    template_name = 'accounts/registration/user_activated.html'


class UserNotActivatedView(views.TemplateView):
    template_name = 'accounts/registration/user_not_activated.html'


class UserLoginView(auth_views.LoginView):
    template_name = 'accounts/login.html'
    redirect_authenticated_user = True


class UserLogoutView(auth_views.LogoutView):
    pass


class UserPasswordResetView(auth_views.PasswordResetView):
    form_class = UserPasswordResetForm
    template_name = 'accounts/password_reset/index.html'
    email_template_name = 'accounts/password_reset/password_reset_email.html'
    success_url = reverse_lazy('accounts:password reset done')


class UserPasswordResetDoneView(auth_views.PasswordResetDoneView):
    template_name = 'accounts/password_reset/password_reset_done.html'


class UserPasswordResetConfirmView(auth_views.PasswordResetConfirmView):
    template_name = 'accounts/password_reset/password_reset_confirm.html'
    success_url = reverse_lazy('accounts:password reset complete')


class UserPasswordResetCompleteView(auth_views.PasswordResetCompleteView):
    template_name = 'accounts/password_reset/password_reset_complete.html'


@login_required
def get_account_details(request):
    profile = Profile.objects.get(user=request.user)
    return render(request, 'accounts/account_details.html', {'profile': profile})


class UserPasswordChangeView(auth_views.PasswordChangeView):
    template_name = 'accounts/password_change/index.html'
    success_url = reverse_lazy('accounts:password change done')


class UserPasswordChangeDoneView(auth_views.PasswordChangeDoneView):
    template_name = 'accounts/password_change/password_change_done.html'


@login_required
def edit_account(request):
    if request.method == 'POST':
        user_form = UserEditForm(request.user, request.POST, instance=request.user)
        profile_form = ProfileEditForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('accounts:details')
    else:
        user_form = UserEditForm(request.user, instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)

    context = {
        'user_form': user_form,
        'profile_form': profile_form,
    }

    return render(request, 'accounts/account_edit.html', context)


@login_required
def delete_account(request):
    if request.method == 'POST':
        form = UserDeleteForm(request.POST, instance=request.user)
        form.instance.is_active = False
        if form.is_valid():
            form.save()
            logout(request)
            return redirect('accounts:delete done')
    else:
        form = UserDeleteForm(instance=request.user)

    return render(request, 'accounts/account_delete/index.html', {'form': form})


class AccountDeleteDoneView(views.TemplateView):
    template_name = 'accounts/account_delete/account_delete_done.html'
