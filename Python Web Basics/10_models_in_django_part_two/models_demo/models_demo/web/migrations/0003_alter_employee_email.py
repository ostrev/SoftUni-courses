# Generated by Django 4.2.2 on 2023-06-07 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_alter_employee_first_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
