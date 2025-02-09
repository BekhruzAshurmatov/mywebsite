# Generated by Django 5.1.4 on 2025-02-09 06:48

import ckeditor_uploader.fields
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0005_student'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='description',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
        migrations.CreateModel(
            name='Tutor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', ckeditor_uploader.fields.RichTextUploadingField()),
                ('image', models.ImageField(upload_to='images/')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.subject')),
            ],
        ),
    ]
