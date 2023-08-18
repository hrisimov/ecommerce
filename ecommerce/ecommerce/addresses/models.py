import uuid

from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()


class Address(models.Model):
    FIRST_NAME_MAX_LENGTH = 30
    LAST_NAME_MAX_LENGTH = 30

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
        max_length=FIRST_NAME_MAX_LENGTH,
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LENGTH,
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
        to=UserModel,
        on_delete=models.CASCADE,
    )

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name_plural = 'Addresses'
