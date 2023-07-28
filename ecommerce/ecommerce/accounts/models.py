import uuid

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


class Address(models.Model):
    PHONE_NUMBER_MAX_LENGTH = 20

    PROVINCE_MAX_LENGTH = 50

    TOWN_CITY_MAX_LENGTH = 50
    TOWN_CITY_VERBOSE_NAME = 'Town/City'

    ADDRESS_LINE_MAX_LENGTH = 150

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )

    first_name = models.CharField(
        max_length=Profile.FIRST_NAME_MAX_LENGTH,
    )

    last_name = models.CharField(
        max_length=Profile.LAST_NAME_MAX_LENGTH,
    )

    phone_number = models.CharField(
        max_length=PHONE_NUMBER_MAX_LENGTH,
    )

    province = models.CharField(
        max_length=PROVINCE_MAX_LENGTH,
    )

    town_city = models.CharField(
        max_length=TOWN_CITY_MAX_LENGTH,
        verbose_name=TOWN_CITY_VERBOSE_NAME,
    )

    address_line = models.CharField(
        max_length=ADDRESS_LINE_MAX_LENGTH,
    )

    default = models.BooleanField(
        default=False,
    )

    user = models.ForeignKey(
        to=EcommerceUser,
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name_plural = 'Addresses'
