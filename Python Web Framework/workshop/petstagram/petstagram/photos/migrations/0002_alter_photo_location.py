# Generated by Django 4.2.2 on 2023-06-08 16:36

from django.db import migrations, models
import petstagram.photos.validators


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='location',
            field=models.CharField(max_length=30, validators=[petstagram.photos.validators.validate_file_size]),
        ),
    ]
