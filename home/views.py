from django.http import HttpResponse
from django.shortcuts import render

from home.models import Setting


# Create your views here.
def index(request):
    setting = Setting.objects.get()
    context = {'setting':setting, 'page':'home'}
    return render(request, 'index.html', context)
def about(request):
    setting = Setting.objects.get()
    context = {'setting':setting, 'page':'about'}
    return render(request, 'about.html', context)
def contact(request):
    setting = Setting.objects.get()
    context = {'setting':setting, 'page':'contact'}
    return render(request, 'contact.html', context)
def service(request):
    setting = Setting.objects.get()
    context = {'setting':setting, 'page':'service'}
    return render(request, 'service.html', context)
def appointment(request):
    setting = Setting.objects.get()
    context = {'setting':setting, 'page':'appointment'}
    return render(request, 'appointment.html', context)
