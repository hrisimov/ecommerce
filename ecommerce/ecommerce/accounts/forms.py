from django import forms
from django.contrib.auth import forms as auth_forms, get_user_model

from ecommerce.accounts.models import Profile
from ecommerce.common.widgets import ImageInput

UserModel = get_user_model()


class UserRegisterForm(auth_forms.UserCreationForm):
    class Meta:
        model = UserModel
        fields = (UserModel.USERNAME_FIELD,)


class UserUpdateForm(auth_forms.UserChangeForm):
    class Meta(auth_forms.UserChangeForm.Meta):
        model = UserModel


class UserDeactivateUpdateForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ()


class UserPasswordResetForm(auth_forms.PasswordResetForm):
    def clean_email(self):
        email = self.cleaned_data['email']
        try:
            UserModel.objects.get(email=email)
            return email
        except UserModel.DoesNotExist:
            raise auth_forms.ValidationError('Error')


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('user',)
        widgets = {
            'photo': ImageInput(),
        }
