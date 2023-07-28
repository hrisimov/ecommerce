from django.core.exceptions import ValidationError


def validate_name(value):
    if not value.isalpha() or not value[0].isupper() or not value[1:].islower():
        raise ValidationError('Ensure the first character is an uppercase letter and others lowercase.')
