from django import forms
from django.contrib.auth import forms as auth_forms, get_user_model
from django.core.exceptions import ObjectDoesNotExist

from ecommerce.accounts.models import Profile

UserModel = get_user_model()


class UserRegistrationForm(auth_forms.UserCreationForm):
    class Meta:
        model = UserModel
        fields = ('email', 'username')


class UserPasswordResetForm(auth_forms.PasswordResetForm):
    def clean_email(self):
        email = self.cleaned_data['email']
        try:
            UserModel.objects.get(email=email)
            return email
        except ObjectDoesNotExist:
            raise auth_forms.ValidationError('Error')


class UserEditForm(forms.ModelForm):
    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user

    def clean_email(self):
        email = self.cleaned_data['email']
        if not email == self.user.email:
            raise auth_forms.ValidationError('Email can not be changed.')
        return email

    class Meta:
        model = UserModel
        fields = ('email', 'username')
        widgets = {
            'email': forms.EmailInput(attrs={'readonly': 'readonly'}),
        }


class UserDeleteForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ()


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name')
