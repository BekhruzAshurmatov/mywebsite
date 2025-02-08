from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models

# Create your models here.
class Setting(models.Model):
    title = models.CharField(max_length=150)
    keywords = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=50)
    address = models.CharField(max_length=100)
    smtp_server = models.CharField(max_length=50)
    smtp_email = models.CharField(max_length=50)
    smtp_password = models.CharField(max_length=10)
    smtp_port = models.CharField(max_length=5)
    youtube = models.CharField(max_length=50)
    instagram = models.CharField(max_length=50)
    facebook = models.CharField(max_length=50)
    icon = models.ImageField(upload_to='images/')
    aboutus = RichTextUploadingField()
    contact = RichTextUploadingField()

    def __str__(self):
        return self.title