from django.core.validators import MinLengthValidator, RegexValidator, MinValueValidator
from django.db import models


# from music_app.web.validators import alphanumeric_validator


# Create your models here.
class Profile(models.Model):
    USERNAME_MAX_LEN = 15
    USERNAME_MIN_LEN = 2

    username = models.CharField(
        max_length=USERNAME_MAX_LEN,
        validators=[
            MinLengthValidator(USERNAME_MIN_LEN),
            RegexValidator('^[a-zA-Z0-9_]*$', message='Username must be Alphanumeric'),
        ],
        null=False,
        blank=False,
    )

    email = models.EmailField(
        null=False,
        blank=False,
    )

    age = models.PositiveIntegerField(
        null=True,
        blank=True,
    )


class Album(models.Model):
    GENRE_MAX_LEN = 30
    NAME_MAX_LEN = 30
    ARTIST_MAX_LEN = 30

    POP_MUSIC = "Pop Music"
    JAZZ_MUSIC = "Jazz Music"
    RNB_MUSIC = "R&B Music"
    ROCK_MUSIC = "Rock Music"
    COUNTRY_MUSIC = "Country Music"
    DANCE_MUSIC = "Dance Music"
    HIP_HOP_MUSIC = "Hip Hop Music"
    OTHER_MUSIC = "Other"

    MUSICS = (
        (POP_MUSIC, POP_MUSIC),
        (JAZZ_MUSIC, JAZZ_MUSIC),
        (RNB_MUSIC, RNB_MUSIC),
        (ROCK_MUSIC, ROCK_MUSIC),
        (COUNTRY_MUSIC, COUNTRY_MUSIC),
        (DANCE_MUSIC, DANCE_MUSIC),
        (HIP_HOP_MUSIC, HIP_HOP_MUSIC),
        (OTHER_MUSIC, OTHER_MUSIC),
    )

    album_name = models.CharField(
        max_length=NAME_MAX_LEN,
        unique=True,
        null=False,
        blank=False,
    )

    artist = models.CharField(
        max_length=ARTIST_MAX_LEN,
        null=False,
        blank=False,
    )

    genre = models.CharField(
        max_length=GENRE_MAX_LEN,
        choices=MUSICS,
        null=False,
        blank=False,
    )

    description = models.TextField(
        null=True,
        blank=True,
    )

    image_url = models.URLField(
        null=False,
        blank=False,
    )

    price = models.FloatField(
        null=False,
        blank=False,
        validators=[
            MinValueValidator(0.0),
        ]
    )

    class Meta:
        ordering = ('pk',)
