from django.contrib import admin
from course.models import Course, Subject, Student, Tutor, SubjectLang, CourseLang, TutorLang


# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']


class SubjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'course', 'image_tag']
    list_filter = ['course']


class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'image_tag']


class TutorAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'image_tag']
    list_filter = ['subject']

class SubjectLanguageAdmin(admin.ModelAdmin):
    list_display = ['title', 'lang', 'slug']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ['lang']

class CourseLanguageAdmin(admin.ModelAdmin):
    list_display = ['title', 'lang', 'slug']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ['lang']

class TutorLanguageAdmin(admin.ModelAdmin):
    list_display = ['name', 'lang', 'slug']
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ['lang']


admin.site.register(Course, CourseAdmin)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Tutor, TutorAdmin)
admin.site.register(SubjectLang, SubjectLanguageAdmin)
admin.site.register(CourseLang, CourseLanguageAdmin)
admin.site.register(TutorLang, TutorLanguageAdmin)