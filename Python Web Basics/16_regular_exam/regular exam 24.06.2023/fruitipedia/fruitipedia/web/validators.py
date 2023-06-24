from django.core.exceptions import ValidationError

ERROR_MESSAGE_FIRST_LETTER = 'Your name must start with a letter!'
ERROR_MESSAGE_ALL_LETTERS = 'Fruit name should contain only letters!!'


def first_char_is_letter_validator(value):
    if not value[0].isalpha():
        raise ValidationError(ERROR_MESSAGE_FIRST_LETTER)


def chars_are_letters_validator(value):
    for char in value:
        if not char.isalpha():
            raise ValidationError(ERROR_MESSAGE_ALL_LETTERS)
