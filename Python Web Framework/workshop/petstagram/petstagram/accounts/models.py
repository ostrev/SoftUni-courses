from django.contrib.auth import models as auth_models
from django.core.validators import MinLengthValidator
from django.db import models
from enum import Enum

from petstagram.accounts.validators import validate_letters


class ChoicesMixin:
    @classmethod
    def choices(cls):
        return [(choice.value, choice.name) for choice in cls]


class ChoicesStringsMixin(ChoicesMixin):
    @classmethod
    def max_length(cls):
        return max(len(x.value) for x in cls)


class Gender(ChoicesStringsMixin, Enum):
    MALE = 'male'
    FEMALE = 'female'
    DO_NOT_SHOW = 'do not show'


class PetstagramUser(auth_models.AbstractUser):
    FIRST_NAME_MAX_LEN = 30
    FIRST_NAME_MIN_LEN = 2
    LAST_NAME_MAX_LEN = 30
    LAST_NAME_MIN_LEN = 2

    email = models.EmailField(unique=True)
    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LEN,
        validators=[
            MinLengthValidator(FIRST_NAME_MIN_LEN),
            validate_letters,
        ]
    )
    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LEN,
        validators=[
            MinLengthValidator(LAST_NAME_MIN_LEN),
            validate_letters,
        ]
    )
    gender = models.CharField(
        choices=Gender.choices(),
        max_length=Gender.max_length(),
        default=Gender.DO_NOT_SHOW,
    )

    profile_picture = models.URLField(
        null=True,
        blank=True,
    )
