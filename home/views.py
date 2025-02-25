from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from course.models import Course, Subject, Tutor, Student, SubjectLang, TutorLang
from home.models import Setting, ContactForm, ContactMessage, SettingLang
from django.contrib import messages
from django.conf import settings
from django.utils import translation


# Create your views here.
def index(request):
    #return HttpResponse('Hello Django!')
    setting = Setting.objects.get(pk=1)
    course = Course.objects.all()
    course_cr = Course.objects.all().order_by('id')[:4]
    subject_cr = Subject.objects.all().order_by('id')[:3]
    tutor_cr = Tutor.objects.all().order_by('id')[:3]

    defaultlang = settings.LANGUAGE_CODE[0:2]
    currentlang = request.LANGUAGE_CODE[0:2]

    if defaultlang != currentlang:
        setting = SettingLang.objects.get(lang=currentlang)
        subject_cr = SubjectLang.objects.filter(lang=currentlang).order_by('subject__id')
        tutor_cr = TutorLang.objects.filter(lang=currentlang).order_by('id')

    page = "home"
    context = {
        'setting': setting,
        'page': page,
        'subject_cr': subject_cr,
        'course_cr': course_cr,
        'course': course,
        'tutor_cr': tutor_cr,
    }
    return render(request, 'index.html', context)


def about(request):
    #return HttpResponse('About us')
    defaultlang = settings.LANGUAGE_CODE[0:2]
    currentlang = request.LANGUAGE_CODE[0:2]
    setting = Setting.objects.get(pk=1)
    if defaultlang != currentlang:
        setting = SettingLang.objects.get(lang=currentlang)

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

    defaultlang = settings.LANGUAGE_CODE[0:2]
    currentlang = request.LANGUAGE_CODE[0:2]
    setting = Setting.objects.get(pk=1)
    if defaultlang != currentlang:
        setting = SettingLang.objects.get(lang=currentlang)

    form = ContactForm
    subject_cr = Subject.objects.all().order_by('id')[:4]
    page = 'home'
    context = {
        'setting': setting,
        'form': form,
        'subject_cr': subject_cr,
        'page': page,
    }
    # return HttpResponse('Contacts page')
    return render(request, 'contact.html', context)


def tutors(request):
    tutor_cr = Tutor.objects.all().order_by('id')
    subject_cr = Subject.objects.all().order_by('id')
    defaultlang = settings.LANGUAGE_CODE[0:2]
    currentlang = request.LANGUAGE_CODE[0:2]
    setting = Setting.objects.get(pk=1)
    if defaultlang != currentlang:
        setting = SettingLang.objects.get(lang=currentlang)
        tutor_cr = TutorLang.objects.filter(lang=currentlang)

    context = {
        'setting': setting,
        'tutor_cr': tutor_cr,
        'subject_cr': subject_cr,
    }
    return render(request, 'tutors.html', context)


def students(request):
    setting = Setting.objects.get()
    student = Student.objects.all()
    context = {
        'setting': setting,
        'student': student,
    }
    return render(request, 'students.html', context)


def subject_details(request, id, slug):
    defaultlang = settings.LANGUAGE_CODE[0:2]
    currentlang = request.LANGUAGE_CODE[0:2]
    # course = Course.objects.all()

    # Находим соответствующий subject_id
    try:
        subject_lang = SubjectLang.objects.get(pk=id)
        subject_id = subject_lang.subject_id  # Берём ID связанного Subject
    except SubjectLang.DoesNotExist:
        subject_id = id  # Если перевода нет, используем переданный ID

    # Теперь ищем Subject по правильному ID
    subject = get_object_or_404(Subject, pk=subject_id)

    setting = Setting.objects.get(pk=1)

    if defaultlang != currentlang:
        try:
            setting = SettingLang.objects.get(lang=currentlang)
            prolang = SubjectLang.objects.get(subject_id=subject_id, lang=currentlang)
            subject.title = prolang.title
            subject.description = prolang.description
            subject.detail = prolang.detail
            subject.subject_tutor = prolang.subject_tutor
        except SubjectLang.DoesNotExist:
            pass
    else:
        subject = get_object_or_404(Subject, pk=id)

    # subject_cr = Subject.objects.all().order_by('id')[:4]
    context = {
        'subject': subject,
        'setting': setting,
        # 'subject_cr': subject_cr,
    }
    return render(request, 'subject_details.html', context)


def subjects(request):
    subject_cr = Subject.objects.all().order_by('id')
    defaultlang = settings.LANGUAGE_CODE[0:2]
    currentlang = request.LANGUAGE_CODE[0:2]
    setting = Setting.objects.get(pk=1)
    if defaultlang != currentlang:
        setting = SettingLang.objects.get(lang=currentlang)
        subject_cr = SubjectLang.objects.filter(lang=currentlang).order_by('subject__id')

    context = {
        'setting': setting,
        'subject_cr': subject_cr,
    }
    return render(request, 'subjects.html', context)


def selectlanguage(request):
    if request.method == 'POST':

        lang = request.POST['language']
        translation.activate(lang)
        request.session[settings.LANGUAGE_COOKIE_NAME] = lang

        return HttpResponseRedirect("/" + lang)




