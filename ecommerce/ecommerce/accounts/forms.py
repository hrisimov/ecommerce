from django.contrib.auth import forms as auth_forms, get_user_model
from django.core.exceptions import ObjectDoesNotExist

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
