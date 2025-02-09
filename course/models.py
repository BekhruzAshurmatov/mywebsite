from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=100)
    keywords = models.CharField(max_length=255)
    description = RichTextUploadingField()
    image = models.ImageField(upload_to='images/')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title


class Subject(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    subject_tutor = models.CharField(max_length=255)
    description = RichTextUploadingField()
    image = models.ImageField(upload_to='images/')
    price = models.CharField(max_length=50)
    detail = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title


class Student(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(max_length=255)
    image = models.ImageField(blank=True, upload_to='images/')

    def __str__(self):
        return self.name


class Tutor(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    description = models.TextField(max_length=255)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name

