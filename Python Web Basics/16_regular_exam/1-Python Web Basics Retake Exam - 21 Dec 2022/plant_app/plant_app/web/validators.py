from django.core.exceptions import ValidationError

CAPITAL_LETTER_MESSAGE = 'Your name must start with a capital letter!'
ALPHA_MESSAGE = 'Plant name should contain only letters!'


def first_letter_is_capital_validator(value):
    if not value[0].isupper():
        raise ValidationError(CAPITAL_LETTER_MESSAGE)


def alpha_validator(value):
    if not value.isalpha():
        raise ValidationError(ALPHA_MESSAGE)
