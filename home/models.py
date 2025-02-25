from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.forms import ModelForm, TextInput, Textarea


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
    aboutus = models.TextField(max_length=255)
    contact = RichTextUploadingField()

    def __str__(self):
        return self.title


class ContactMessage(models.Model):
    STATUS = (
        ('New', 'New'),
        ('Read', 'Read'),
        ('Closed', 'Closed'),
    )
    name = models.CharField(max_length=20)
    phone = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)
    message = models.TextField(max_length=255)
    status = models.CharField(max_length=10, choices=STATUS, default='New')
    ip = models.CharField(max_length=20)
    note = models.CharField(max_length=100)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class ContactForm(ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'phone', 'subject', 'message']
        widgets = {
            'name': TextInput(attrs={'class': 'input', 'placeholder': 'Name & Surname'}),
            'subject': TextInput(attrs={'class': 'input', 'placeholder': 'Subject'}),
            'phone': TextInput(attrs={'class': 'input', 'placeholder': 'Phone Number'}),
            'message': Textarea(attrs={'class': 'input', 'placeholder': 'Your Message', 'rows': '5'}),
        }


class Language(models.Model):
    name = models.CharField(max_length=20)
    code = models.CharField(max_length=5)
    status = models.BooleanField()

    def __str__(self):
        return self.name

llist = Language.objects.all()
list1 = []
for rs in llist:
    list1.append((rs.code, rs.name))
langlist = (list1)


class SettingLang(models.Model):
    setting = models.ForeignKey(Setting, on_delete=models.CASCADE)
    lang = models.CharField(max_length=6, choices=langlist)
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
    aboutus = models.TextField(max_length=255)
    contact = RichTextUploadingField()

    def __str__(self):
        return self.title