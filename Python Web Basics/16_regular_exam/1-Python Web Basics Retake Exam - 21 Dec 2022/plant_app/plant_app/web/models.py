from django.core.validators import MinLengthValidator
from django.db import models

from plant_app.web.validators import first_letter_is_capital_validator, alpha_validator


# Create your models here.
class Profile(models.Model):
    USERNAME_MAX_LEN = 10
    USERNAME_MIN_LEN = 2

    FIRST_NAME_MAX_LEN = 20
    LAST_NAME_MAX_LEN = 20

    username = models.CharField(
        max_length=USERNAME_MAX_LEN,
        validators=[
            MinLengthValidator(USERNAME_MIN_LEN),
        ],
        null=False,
        blank=False
    )

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LEN,
        validators=[
            first_letter_is_capital_validator,
        ],
        null=False,
        blank=False,
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LEN,
        validators=[
            first_letter_is_capital_validator,
        ],
        null=False,
        blank=False,
    )

    profile_picture = models.URLField(
        null=True,
        blank=True,
    )


class Plant(models.Model):
    PLANT_TYPE_MAX_LEN = 14
    NAME_MAX_LEN = 20
    NAME_MIN_LEN = 2

    OUTDOOR = "Outdoor Plants"
    INDOR = "Indoor Plants"

    TYPE = [
        (OUTDOOR, OUTDOOR),
        (INDOR, INDOR),
    ]

    plant_type = models.CharField(
        max_length=PLANT_TYPE_MAX_LEN,
        choices=TYPE,
        null=False,
        blank=False,
    )

    name = models.CharField(
        max_length=NAME_MAX_LEN,
        validators=[
            MinLengthValidator(NAME_MIN_LEN),
            alpha_validator,
        ],
        null=False,
        blank=False,
    )

    image = models.URLField(
        null=False,
        blank=False,
    )

    description = models.TextField(
        null=False,
        blank=False,
    )

    price = models.FloatField(
        null=False,
        blank=False,
    )

    class Meta:
        ordering = ('id',)

