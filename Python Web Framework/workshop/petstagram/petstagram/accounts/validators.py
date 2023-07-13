from django.core.exceptions import ValidationError


def validate_letters(value):
    for char in value:
        if not char.isalpha():
            raise ValidationError("ValidationError")