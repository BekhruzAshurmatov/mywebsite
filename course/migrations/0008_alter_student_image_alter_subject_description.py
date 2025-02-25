# Generated by Django 5.1.4 on 2025-02-17 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0007_alter_student_description_alter_tutor_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='subject',
            name='description',
            field=models.TextField(max_length=255),
        ),
    ]
