# Generated by Django 5.1.4 on 2025-02-08 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='description',
            field=models.TextField(max_length=255),
        ),
        migrations.AlterField(
            model_name='subject',
            name='price',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='subject',
            name='title',
            field=models.CharField(max_length=255),
        ),
    ]
