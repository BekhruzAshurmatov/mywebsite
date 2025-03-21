# Generated by Django 5.1.4 on 2025-02-17 11:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0009_subjectlang'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseLang',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lang', models.CharField(choices=[('en', 'English'), ('ru', 'Russian'), ('uz', 'Uzbek')], max_length=6)),
                ('title', models.CharField(max_length=150)),
                ('keywords', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('slug', models.SlugField(unique=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.course')),
            ],
        ),
    ]
