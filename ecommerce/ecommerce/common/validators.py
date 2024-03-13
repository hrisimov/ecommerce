from django.core.exceptions import ValidationError
from django.core.validators import BaseValidator
from django.utils.deconstruct import deconstructible


def validate_name(value):
    if not value.isalpha() or not value[0].isupper() or not value[1:].islower():
        raise ValidationError('Ensure the first character is an uppercase letter and others lowercase.')


@deconstructible
class MaxFileSizeInMbValidator(BaseValidator):
    message = 'The file is too large. Max size is %(limit_value)s MB.'

    @staticmethod
    def __megabytes_to_bytes(value):
        return value * 1024 * 1024

    def compare(self, a, b):
        return a > self.__megabytes_to_bytes(b)

    def clean(self, x):
        return x.size
