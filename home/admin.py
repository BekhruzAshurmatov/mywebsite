from django.contrib import admin
from home.models import Setting, ContactMessage


# Register your models here.
class SettingAdmin(admin.ModelAdmin):
    list_display = ['title']

class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'status']

admin.site.register(Setting, SettingAdmin)
admin.site.register(ContactMessage, ContactMessageAdmin)