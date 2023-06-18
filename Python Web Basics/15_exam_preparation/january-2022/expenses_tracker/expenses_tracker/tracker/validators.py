from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible

VALIDATE_LETTERS_ERROR_MESSAGE = "ValidationError"


def validate_letters(value):
    for char in value:
        if not char.isalpha():
            raise ValidationError(VALIDATE_LETTERS_ERROR_MESSAGE)


@deconstructible
class MaxFileSizeValidator:
    def __init__(self, max_size):
        self.max_size = max_size

    def __call__(self, value):
        file_size = value.file.size
        if file_size > self.__megabytes_to_bytes(self.max_size):
            raise ValidationError(self.__exception_message())

    @staticmethod
    def __megabytes_to_bytes(value):
        return value * 1024 * 1024

    def __exception_message(self):
        return f'Max file size is {self.max_size:.2f} MB'
