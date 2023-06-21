from django.core.exceptions import ValidationError


def year_validator(value):
    MIN_YEAR = 1980
    MAX_YEAR = 2049
    VALIDATION_ERROR_MESSAGE = f"Year must be between {MIN_YEAR} and {MAX_YEAR}"
    if not MIN_YEAR <= value <= MAX_YEAR:
        raise ValidationError(VALIDATION_ERROR_MESSAGE)
