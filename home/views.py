from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    #return HttpResponse('Hello Django!')
    return render(request, 'index.html')


def about(request):
    return HttpResponse('About us')


def contact(request):
    return HttpResponse('Contacts page')