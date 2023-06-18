from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from expenses_tracker.tracker.validators import validate_letters, MaxFileSizeValidator


# Create your models here.
class Profile(models.Model):
    FIRST_NAME_MIN_LEN = 2
    FIRST_NAME_MAX_LEN = 15

    LAST_NAME_MIN_LEN = 2
    LAST_NAME_MAX_LEN = 15

    DEFAULT_BUDGET = 0
    MIN_BUDGET = 0

    MAX_FILE_SIZE = 5

    first_name = models.CharField(
        blank=False,
        null=False,
        max_length=FIRST_NAME_MAX_LEN,
        validators=[
            MinLengthValidator(FIRST_NAME_MIN_LEN),
            validate_letters
        ],
    )
    last_name = models.CharField(
        blank=False,
        null=False,
        max_length=LAST_NAME_MAX_LEN,
        validators=[
            MinLengthValidator(LAST_NAME_MIN_LEN),
            validate_letters
        ],
    )
    budget = models.FloatField(
        blank=False,
        null=False,
        default=DEFAULT_BUDGET,
        validators=[
            MinValueValidator(MIN_BUDGET)
        ],
    )
    profile_image = models.ImageField(
        upload_to='profile_pic',
        blank=True,
        null=True,
        validators=[MaxFileSizeValidator(MAX_FILE_SIZE)]
    )


class Expense(models.Model):
    TITLE_MAX_LEN = 30

    title = models.CharField(
        blank=False,
        null=False,
        max_length=TITLE_MAX_LEN,
    )
    expense_image = models.URLField(
        blank=False,
        null=False,
        verbose_name='Link to image'
    )
    description = models.TextField(
        blank=True,
        null=True,
    )
    price = models.FloatField(
        blank=False,
        null=False,
    )

    class Meta:
        ordering = ('title', 'price')
