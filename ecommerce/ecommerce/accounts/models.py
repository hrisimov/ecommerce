from django.contrib.auth import models as auth_models
from django.db import models

from ecommerce.accounts.managers import EcommerceUserManager
from ecommerce.common.validators import validate_name, MaxFileSizeInMbValidator


class EcommerceUser(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
    email = models.EmailField(
        unique=True,
        error_messages={
            'unique': 'A user with that email already exists.',
        },
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


class Profile(models.Model):
    FIRST_NAME_MAX_LENGTH = 30

    LAST_NAME_MAX_LENGTH = 30

    PHOTO_MAX_SIZE_MB = 5
    PHOTO_UPLOAD_TO_DIR = 'profile_photos/'

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

    photo = models.ImageField(
        upload_to=PHOTO_UPLOAD_TO_DIR,
        null=True,
        blank=True,
        validators=(
            MaxFileSizeInMbValidator(PHOTO_MAX_SIZE_MB),
        ),
    )

    user = models.OneToOneField(
        to=EcommerceUser,
        on_delete=models.CASCADE,
        primary_key=True,
    )
