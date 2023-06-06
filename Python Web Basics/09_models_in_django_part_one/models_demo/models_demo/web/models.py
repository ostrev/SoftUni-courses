from django.db import models


# Create your models here.
class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=40, null=True)

    review = models.TextField()
    years_of_experience = models.IntegerField()
    years_of_experience2 = models.PositiveIntegerField()
    created_on = models.DateTimeField(auto_now_add=True)
    update_on = models.DateTimeField(auto_now=True)

    start_date = models.DateField()
    email = models.EmailField()




# Employee.objects.all()
# Employee.objects.filter()
# Employee.objects.create()
# Employee.objects.update()
