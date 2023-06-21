from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from car_collection.web.validators import year_validator


class Profile(models.Model):
    USERNAME_MAX_LEN = 10
    USERNAME_MIN_LEN = 2
    USERNAME_MESSAGE_ERROR = f"The username must be a minimum of {USERNAME_MIN_LEN} chars"
    PASSWORD_MAX_LEN = 30
    FIRST_NAME_MAX_LEN = 30
    LAST_NAME_MAX_LEN = 30
    AGE_MIN_VALUE = 18

    username = models.CharField(
        max_length=USERNAME_MAX_LEN,
        validators=[
            MinLengthValidator(
                USERNAME_MIN_LEN,
                message=USERNAME_MESSAGE_ERROR
            )
        ]
    )
    email = models.EmailField()
    age = models.PositiveIntegerField(
        validators=[
            MinValueValidator(AGE_MIN_VALUE)
        ],
    )
    password = models.CharField(
        max_length=PASSWORD_MAX_LEN
    )  # TODO in Form
    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LEN,
        null=True,
        blank=True,
    )
    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LEN,
        null=True,
        blank=True,
    )
    profile_picture = models.URLField(
        null=True,
        blank=True,
    )


class Car(models.Model):
    TYPE_MAX_LEN = 10
    MODEL_MAX_LEN = 20
    MODEL_MIN_LEN = 2
    PRICE_MIN_VALUE = 1

    SPORT_CAR = "Sports Car"
    PICKUP = "Pickup"
    CROSSOVER = "Crossover"
    MINIBUS = "Minibus"
    OTHERS = "Other"

    CARS = [
        (SPORT_CAR, SPORT_CAR),
        (PICKUP, PICKUP),
        (CROSSOVER, CROSSOVER),
        (MINIBUS, MINIBUS),
        (OTHERS, OTHERS),
    ]

    type = models.CharField(
        max_length=TYPE_MAX_LEN,
        choices=CARS,
    )
    model = models.CharField(
        max_length=MODEL_MAX_LEN,
        validators=[
            MinLengthValidator(MODEL_MIN_LEN),
        ]
    )
    year = models.IntegerField(
        validators=[
            year_validator,
        ]
    )
    image = models.URLField(
        verbose_name='Image URL'
    )
    price = models.FloatField(
        validators=[
            MinValueValidator(PRICE_MIN_VALUE),
        ]
    )

    class Meta:
        ordering = ('id',)

