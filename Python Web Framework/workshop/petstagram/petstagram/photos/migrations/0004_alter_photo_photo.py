# Generated by Django 4.2.2 on 2023-06-08 17:11

from django.db import migrations, models
import petstagram.photos.validators


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0003_alter_photo_location_alter_photo_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='photo',
            field=models.ImageField(upload_to='mediafiles/photos', validators=[petstagram.photos.validators.validate_file_size]),
        ),
    ]