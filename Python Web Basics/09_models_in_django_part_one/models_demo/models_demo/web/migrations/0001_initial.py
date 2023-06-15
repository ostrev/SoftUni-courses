# Generated by Django 4.2.2 on 2023-06-05 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=40, null=True)),
                ('review', models.TextField()),
                ('years_of_experience', models.IntegerField()),
                ('years_of_experience2', models.PositiveIntegerField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('update_on', models.DateTimeField(auto_now=True)),
                ('start_date', models.DateField()),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]