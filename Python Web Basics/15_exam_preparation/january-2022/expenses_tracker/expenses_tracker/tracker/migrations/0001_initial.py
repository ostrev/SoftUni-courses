# Generated by Django 4.2.2 on 2023-06-17 20:59

import django.core.validators
from django.db import migrations, models
import expenses_tracker.tracker.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('expense_image', models.URLField()),
                ('description', models.TextField(blank=True, null=True)),
                ('price', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=15, validators=[django.core.validators.MinLengthValidator(2), expenses_tracker.tracker.validators.validate_letters])),
                ('last_name', models.CharField(max_length=15, validators=[django.core.validators.MinLengthValidator(2), expenses_tracker.tracker.validators.validate_letters])),
                ('budget', models.FloatField(default=0, validators=[django.core.validators.MinLengthValidator(0)])),
                ('profile_image', models.ImageField(blank=True, default='user.png', null=True, upload_to='profile_pic', validators=[expenses_tracker.tracker.validators.MaxFileSizeValidator(5)])),
            ],
        ),
    ]
