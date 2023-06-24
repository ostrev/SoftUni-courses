from django.core.validators import MinLengthValidator
from django.db import models

from fruitipedia.web.validators import first_char_is_letter_validator, chars_are_letters_validator


#
class Profile(models.Model):
    FIRST_NAME_MAX_LEN = 25
    FIRST_NAME_MIN_LEN = 2
    LAST_NAME_MAX_LEN = 35
    LAST_NAME_MIN_LEN = 1
    EMAIL_MAX_LEN = 40
    PASSWORD_MAX_LEN = 20
    PASSWORD_MIN_LEN = 8
    AGE_DEFAULT_VALUE = 18

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LEN,
        validators=[
            MinLengthValidator(FIRST_NAME_MIN_LEN),
            first_char_is_letter_validator,
        ]
    )
    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LEN,
        validators=[
            MinLengthValidator(LAST_NAME_MIN_LEN),
            first_char_is_letter_validator,
        ]
    )
    email = models.EmailField(max_length=EMAIL_MAX_LEN)
    password = models.CharField(
        max_length=LAST_NAME_MAX_LEN,
        validators=[MinLengthValidator(PASSWORD_MIN_LEN), ]
    )
    image = models.URLField(
        null=True,
        blank=True,
        verbose_name='Image URL'
    )
    age = models.IntegerField(
        null=True,
        blank=True,
        default=AGE_DEFAULT_VALUE
    )


class Fruit(models.Model):
    NAME_MAX_LEN = 30
    NAME_MIN_LEN = 2

    name = models.CharField(
        max_length=NAME_MAX_LEN,
        validators=[
            MinLengthValidator(NAME_MIN_LEN),
            chars_are_letters_validator,
        ]
    )
    image = models.URLField(
        verbose_name='Image URL'
    )
    description = models.TextField()
    nutrition = models.TextField(
        null=True,
        blank=True,
    )

    class Meta:
        ordering = ('id',)
