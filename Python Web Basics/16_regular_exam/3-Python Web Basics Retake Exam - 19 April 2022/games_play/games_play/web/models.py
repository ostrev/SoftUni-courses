from django.core.validators import MinValueValidator
from django.db import models

from games_play.web.validators import rating_validator


# Create your models here.
class Profile(models.Model):
    AGE_MIN_VALUE = 12
    PASSWORD_MAX_LEN = 30
    FIRST_NAME_MAX_LEN = 30
    LAST_NAME_MAX_LEN = 30

    email = models.EmailField()
    age = models.PositiveIntegerField(
        validators=[MinValueValidator(AGE_MIN_VALUE)]
    )
    password = models.CharField(
        max_length=PASSWORD_MAX_LEN
    )
    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LEN,
        null=True,
        blank=True,
        verbose_name='First Name'
    )
    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LEN,
        null=True,
        blank=True,
        verbose_name='Last Name'
    )
    profile_image = models.URLField(
        null=True,
        blank=True,
        verbose_name='Profile Picture'
    )


class Game(models.Model):
    TITLE_MAX_LEN = 30
    CATEGORY_MAX_LEN = 15
    MAX_LEVEL_MIN_VALUE = 1

    ACTION = "Action"
    ADVENTURE = "Adventure"
    PUZZLE = "Puzzle"
    STRATEGY = "Strategy"
    SPORTS = "Sports"
    BOARD_CARD = "Board/Card Game"
    OTHER = "Other"

    GAMES = (
        (ACTION, ACTION),
        (ADVENTURE, ADVENTURE),
        (PUZZLE, PUZZLE),
        (STRATEGY, STRATEGY),
        (SPORTS, SPORTS),
        (BOARD_CARD, BOARD_CARD),
        (OTHER, OTHER)
    )

    title = models.CharField(
        max_length=TITLE_MAX_LEN,
        unique=True,
    )
    category = models.CharField(
        max_length=CATEGORY_MAX_LEN,
        choices=GAMES,
    )
    rating = models.FloatField(
        validators=[
            rating_validator,
        ]
    )
    max_level = models.IntegerField(
        validators=[
            MinValueValidator(MAX_LEVEL_MIN_VALUE)
        ],
        null=True,
        blank=True,
    )
    image = models.URLField(
        verbose_name='Image URL'
    )
    summary = models.TextField(
        null=True,
        blank=True,
    )

    class Meta:
        ordering = ['id']
