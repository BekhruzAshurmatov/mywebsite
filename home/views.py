from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from course.models import Course, Subject, Tutor, Student
from home.models import Setting, ContactForm, ContactMessage
from django.contrib import messages
from django.conf import settings
from django.utils import translation


# Create your views here.
def index(request):
    #return HttpResponse('Hello Django!')
    setting = Setting.objects.get()
    course = Course.objects.all()
    course_cr = Course.objects.all().order_by('id')[:4]
    subject_cr = Subject.objects.all().order_by('id')
    tutor_cr = Tutor.objects.all().order_by('id')[:3]
    page = "home"
    context = {'setting': setting,
               'page': page,
               'subject_cr': subject_cr,
               'course_cr': course_cr,
               'course': course,
               'tutor_cr': tutor_cr, }
    return render(request, 'index.html', context)


def about(request):
    #return HttpResponse('About us')
    setting = Setting.objects.get()
    context = {'setting': setting}
    return render(request, 'about.html', context)


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            data = ContactMessage()
            data.name = form.cleaned_data['name']
            data.phone = form.cleaned_data['phone']
            data.subject = form.cleaned_data['subject']
            data.message = form.cleaned_data['message']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()
            messages.success(request, "Thanks, " + data.name + " We received your message and will respond shortly...")
            return HttpResponseRedirect('/contact')

    setting = Setting.objects.get()
    form = ContactForm
    context = {'setting': setting, }
    # return HttpResponse('Contacts page')
    return render(request, 'contact.html', context)


def tutors(request):
    setting = Setting.objects.get()
    tutor = Tutor.objects.all()
    context = {'setting': setting,
               'tutor': tutor, }
    return render(request, 'tutors.html', context)


def students(request):
    setting = Setting.objects.get()
    student = Student.objects.all()
    context = {'setting': setting,
               'student': student, }
    return render(request, 'students.html', context)


def subject_details(request, id, slug):
    course = Course.objects.all()
    subject = Subject.objects.get(pk=id)
    tutor = Tutor.objects.get(subject=subject)
    context = {'subject': subject,
               'course': course,
               'tutor': tutor, }
    return render(request, 'subject_details.html', context)

def subjects(request):
    setting = Setting.objects.get()
    subjects_cr = Subject.objects.all()
    context = {'setting': setting,
               'subjects_cr': subjects_cr, }
    return render(request, 'subjects.html', context)

def selectlanguage(request):
    if request.method == 'POST':

        lang = request.POST['language']
        translation.activate(lang)
        request.session[settings.LANGUAGE_COOKIE_NAME] = lang
        return HttpResponseRedirect("/" + lang)




