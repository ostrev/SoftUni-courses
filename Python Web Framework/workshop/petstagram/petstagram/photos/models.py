from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator
from django.db import models

from petstagram.pets.models import Pet
from petstagram.photos.validators import validate_file_size

UserModel = get_user_model()


class Photo(models.Model):
    photo = models.ImageField(
        validators=(validate_file_size,),
        upload_to='photos/',
    )
    description = models.TextField(
        max_length=300,
        validators=(MinLengthValidator(10),),
        blank=True,
        null=True,
    )
    location = models.CharField(max_length=30, blank=True, null=True)
    tagged_pets = models.ManyToManyField(Pet, blank=True)
    date_of_publication = models.DateField(auto_now=True)

    user = models.ForeignKey(UserModel, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"{self.id} - {self.photo}"
