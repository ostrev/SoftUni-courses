# Generated by Django 4.2.2 on 2023-06-08 16:39

from django.db import migrations, models
import petstagram.photos.validators


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0002_alter_photo_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='location',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='photo',
            name='photo',
            field=models.ImageField(upload_to='', validators=[petstagram.photos.validators.validate_file_size]),
        ),
    ]