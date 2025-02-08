from django.contrib import admin
from course.models import Course, Subject

# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']


class SubjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'course', 'slug']
    list_filter = ['course']

admin.site.register(Course, CourseAdmin)
admin.site.register(Subject, SubjectAdmin)