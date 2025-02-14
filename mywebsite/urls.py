"""
URL configuration for mywebsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from home.views import index, about, contact, tutors, students, subject_details, subjects, selectlanguage
from course import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import gettext_lazy as _

urlpatterns = [
    path('selectlanguage', selectlanguage, name='selectlanguage'),
    path('i18n/', include('django.conf.urls.i18n')),
]
urlpatterns += i18n_patterns(
    path(_('admin/'), admin.site.urls),
    path('home/', index, name='home'),
    path('', index, name='home'),
    path('course/', views.index, name='course'),
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('about.html', about, name='about'),
    path('contact.html', contact, name='contact'),
    path('tutors.html', tutors, name='tutor'),
    path('students.html', students, name='student'),
    path('courses.html', subjects, name='subject'),
    path('subject/<int:id>/<slug:slug>', subject_details, name='subject_detail'),
    path('tutor/<int:id>/<slug:slug>', subject_details, name='subject_detail'),
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
