# Generated by Django 4.2.2 on 2023-06-07 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_alter_employee_review'),
    ]

    operations = [
        migrations.CreateModel(
            name='NullBlankDemo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blank', models.IntegerField(blank=True)),
                ('null', models.IntegerField(null=True)),
                ('blank_null', models.IntegerField(blank=True, null=True)),
                ('default', models.IntegerField()),
            ],
        ),
    ]