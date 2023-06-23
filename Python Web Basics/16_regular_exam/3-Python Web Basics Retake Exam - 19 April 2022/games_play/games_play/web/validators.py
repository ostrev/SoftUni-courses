from django.core.exceptions import ValidationError


def rating_validator(value):
    MIN_VALUE = 0.1
    MAX_VALUE = 5.0
    if not MIN_VALUE <= value <= MAX_VALUE:
        raise ValidationError

