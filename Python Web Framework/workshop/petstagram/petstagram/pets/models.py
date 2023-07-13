from django.contrib.auth import get_user_model
from django.db import models
from django.template.defaultfilters import slugify
from django.utils.text import slugify

UserModel = get_user_model()

# Create your models here.
class Pet(models.Model):
    name = models.CharField(max_length=30)
    date_of_birth = models.DateField(blank=True, null=True)
    personal_photo = models.URLField()
    slug = models.SlugField(unique=True, blank=True, null=True)

    user = models.ForeignKey(UserModel, on_delete=models.DO_NOTHING)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.slug:
            self.slug = slugify(f"{self.name}-{self.id}")
        return super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.name} - id {self.pk}'