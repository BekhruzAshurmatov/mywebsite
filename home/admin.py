from django.contrib import admin
from home.models import Setting, ContactMessage, Language, SettingLang


# Register your models here.
class SettingAdmin(admin.ModelAdmin):
    list_display = ['title']

class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'status']

class LanguagesAdmin(admin.ModelAdmin):
    list_display = ['name', 'code', 'status']
    list_filter = ['status']

class SettingLangAdmin(admin.ModelAdmin):
    list_display = ['title', 'keywords', 'description', 'lang']
    list_filter = ['lang']

admin.site.register(Setting, SettingAdmin)
admin.site.register(ContactMessage, ContactMessageAdmin)
admin.site.register(Language, LanguagesAdmin)
admin.site.register(SettingLang, SettingLangAdmin)