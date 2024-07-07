# Generated by Django 4.1.3 on 2024-07-06 11:27

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('azayd', '0002_blog'),
    ]

    operations = [
        migrations.CreateModel(
            name='Career',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jobTitle', models.CharField(max_length=255)),
                ('jobSalary', models.CharField(max_length=255)),
                ('jobSkills', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=255), size=None)),
                ('jobEmail', models.CharField(max_length=25)),
            ],
        ),
    ]