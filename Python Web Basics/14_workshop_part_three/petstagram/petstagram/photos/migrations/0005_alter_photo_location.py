# Generated by Django 4.2.2 on 2023-06-08 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0004_alter_photo_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='location',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
