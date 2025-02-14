from django.contrib import admin
from course.models import Course, Subject, Student, Tutor



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


admin.site.register(Course, CourseAdmin)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Tutor, TutorAdmin)