from django.db import models


# Create your models here.

class Task(models.Model):
    # varchar(30)
    task_title = models.CharField(max_length=50)
    task_text = models.TextField()
