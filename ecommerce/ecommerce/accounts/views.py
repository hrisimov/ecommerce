from django.contrib.auth import get_user_model, views as auth_views
from django.contrib.sites.shortcuts import get_current_site
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

from .forms import UserRegistrationForm
from .tasks import send_account_activation_email
from .tokens import account_activation_token

UserModel = get_user_model()


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            current_site = get_current_site(request)
            message = render_to_string('accounts/registration/account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            send_account_activation_email.delay(message, user.email)
            return render(request, 'accounts/registration/account_created.html', {'user': user})
    else:
        form = UserRegistrationForm()
    return render(request, 'accounts/registration/index.html', {'form': form})


def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = UserModel.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, ObjectDoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        return render(request, 'accounts/registration/account_activated.html')
    else:
        return render(request, 'accounts/registration/account_not_activated.html')


class UserLoginView(auth_views.LoginView):
    template_name = 'accounts/login.html'
    redirect_authenticated_user = True


class UserLogoutView(auth_views.LogoutView):
    pass
