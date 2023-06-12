from django.db import models

from forms_demos_two.web.validators import validate_text, ValueInRangeValidator


class Person(models.Model):
    MAX_NAME_LENGTH = 20
    name = models.CharField(max_length=MAX_NAME_LENGTH)

    profile_image = models.ImageField(
        upload_to='persons',
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.name


# Create your models here.
class Todo(models.Model):
    MAX_TODOS_COUNT_PER_PERSON = 3
    MAX_TEXT_LENGTH = 25
    text = models.CharField(
        max_length=MAX_TEXT_LENGTH,
        validators=(validate_text,),
        null=False,
        blank=False,
    )

    priority = models.IntegerField(
        null=False,
        blank=False,
        validators=(ValueInRangeValidator(1, 10),)
    )

    is_done = models.BooleanField(
        null=False,
        blank=False,
        default=False,
    )

    assignee = models.ForeignKey(
        Person,
        on_delete=models.RESTRICT,
    )
