from django.contrib.auth import models as auth_models
from django.contrib.auth import validators as auth_validators
from django.core import validators
from django.db import models

from ecommerce.accounts.managers import EcommerceUserManager
from ecommerce.common.validators import validate_name


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


class Profile(models.Model):
    FIRST_NAME_MAX_LENGTH = 30

    LAST_NAME_MAX_LENGTH = 30

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LENGTH,
        null=True,
        blank=True,
        validators=(validate_name,),
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LENGTH,
        null=True,
        blank=True,
        validators=(validate_name,),
    )

    user = models.OneToOneField(
        to=EcommerceUser,
        on_delete=models.CASCADE,
        primary_key=True,
    )
