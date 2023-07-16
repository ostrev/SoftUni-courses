from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()

# Create your models here.
class Article(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=50, null=False, blank=False)

# class Profile(models.Model):
#     first_name = models.CharField(max_length=30)
#     # ....
#
#     UserModel = models.OneToOneField(UserModel, on_delete=models.CASCADE)
#