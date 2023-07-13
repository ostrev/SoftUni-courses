from django.contrib.auth import get_user_model
from django.db import models

from petstagram.photos.models import Photo

UserModel =get_user_model()
# Create your models here.
class Comment(models.Model):
    comment_text = models.TextField(max_length=300, )
    date_time_of_publication = models.DateTimeField(auto_now_add=True)
    to_photo = models.ForeignKey(Photo, on_delete=models.CASCADE)

    user = models.ForeignKey(UserModel, on_delete=models.DO_NOTHING)

    class Meta:
        ordering = ['-date_time_of_publication']


class Like(models.Model):
    to_photo = models.ForeignKey(Photo, on_delete=models.CASCADE)

    user = models.ForeignKey(UserModel, on_delete=models.DO_NOTHING)