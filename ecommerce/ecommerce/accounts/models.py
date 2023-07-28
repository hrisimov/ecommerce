from django.contrib.auth import models as auth_models
from django.contrib.auth import validators as auth_validators
from django.core import validators
from django.db import models

from ecommerce.accounts.managers import EcommerceUserManager


class EcommerceUser(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
    USERNAME_MAX_LENGTH = 50

    email = models.EmailField(
        unique=True,
        validators=(validators.EmailValidator(),),
    )

    username = models.CharField(
        max_length=USERNAME_MAX_LENGTH,
        unique=True,
        validators=(auth_validators.UnicodeUsernameValidator(),),
    )

    is_staff = models.BooleanField(
        default=False,
    )

    is_active = models.BooleanField(
        default=False,
    )

    date_joined = models.DateTimeField(
        auto_now_add=True,
    )

    objects = EcommerceUserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('username',)
