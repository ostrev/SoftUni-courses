# Generated by Django 4.2.2 on 2023-06-07 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_nullblankdemo'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='is_full_time',
            field=models.BooleanField(null=True),
        ),
    ]
