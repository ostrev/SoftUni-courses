from django.core.exceptions import ValidationError
# from django.core.validators import RegexValidator

ALPHANUMERIC_VALIDATOR_MESSAGE = 'Ensure this value contains only letters, numbers, and underscore.'


def alphanumeric_validator(value):
    for char in value:
        if not char.isalnum() and '_' not in value:
            raise ValidationError(ALPHANUMERIC_VALIDATOR_MESSAGE)

# works in model
# RegexValidator('^[a-zA-Z0-9_]*$', message='Username must be Alphanumeric'),
