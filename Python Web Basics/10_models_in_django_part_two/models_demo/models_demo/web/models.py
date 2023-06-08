from datetime import date
from django.db import models
from django.urls import reverse

from models_demo.web.validators import validate_in_the_past


class AuditInfo(models.Model):
    class Meta:
        abstract = True

    created_on = models.DateTimeField(auto_now_add=True)
    update_on = models.DateTimeField(auto_now=True)


class Department(AuditInfo, models.Model):
    name = models.CharField(max_length=20)
    slug = models.SlugField(unique=True)


    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        url = reverse('department details', kwargs={
            'pk': self.pk,
            'slug': self.slug,
        })
        return url


class Project(AuditInfo, models.Model):
    name = models.CharField(max_length=20)
    code_name = models.CharField(max_length=10, unique=True)
    deadline = models.DateField()

    def __str__(self):
        return f'{self.name}'


class Employee(AuditInfo, models.Model):
    class Meta:
        ordering = ['-years_of_experience']

    LEVEL_JUNIOR = "Junior"
    LEVEL_REGULAR = "Regular"
    LEVEL_SENIOR = "Senior"

    LEVELS = (
        (LEVEL_JUNIOR, LEVEL_JUNIOR),
        (LEVEL_REGULAR, LEVEL_REGULAR),
        (LEVEL_SENIOR, LEVEL_SENIOR),
    )

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=40, null=True)

    review = models.TextField(default='Test')
    years_of_experience = models.IntegerField()
    years_of_experience2 = models.PositiveIntegerField()

    is_full_time = models.BooleanField(null=True)

    level = models.CharField(
        max_length=25,
        # choices=(
        #     ('jr', 'Junior'),
        #     ('reg', 'Regular'),
        #     ('sr', 'Senior')
        # )
        choices=LEVELS,
        verbose_name='Level_exp'
    )

    start_date = models.DateField(
        validators=(validate_in_the_past,)
    )
    email = models.EmailField(unique=True)

    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
    )

    projects = models.ManyToManyField(
        Project,
        # through='EmployeesProjects'
    )

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def years_of_employment(self):
        return date.today() - self.start_date

    def __str__(self):
        return f"ID: {self.pk} | Name: {self.full_name}"


class AccessCard(models.Model):
    employee = models.OneToOneField(
        Employee,
        on_delete=models.CASCADE,
        primary_key=True,
    )


class Category(AuditInfo, models.Model):
    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=15, )
    parent_category = models.ForeignKey(
        'Category',
        on_delete=models.RESTRICT,
        null=True,
        blank=True,
    )

    def __str__(self):
        return f'{self.name}'


# Employee.objects.all()
# Employee.objects.filter()
# Employee.objects.create()
# Employee.objects.update()


class NullBlankDemo(models.Model):
    blank = models.IntegerField(
        blank=True,
        null=False,
    )
    null = models.IntegerField(
        blank=False,
        null=True,
    )
    blank_null = models.IntegerField(
        blank=True,
        null=True,
    )
    default = models.IntegerField(
        blank=False,
        null=False,
    )

    def __str__(self):
        return f"null blank demo"


class EmployeesProjects(models.Model):
    employee_id = models.ForeignKey(Employee, on_delete=models.RESTRICT)
    project_id = models.ForeignKey(Project, on_delete=models.RESTRICT)

    date_join = models.DateField(auto_now_add=True)
