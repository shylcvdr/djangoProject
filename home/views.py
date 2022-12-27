from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from home.forms import SignUpForm
from home.models import Setting, ContactFormMessage, ContactFormu


# Create your views here.
def index(request):
    setting = Setting.objects.get()
    context = {'setting':setting, 'page':'home'}
    return render(request, 'index.html', context)
def about(request):
    setting = Setting.objects.get()
    context = {'setting':setting, 'page':'about'}
    return render(request, 'about.html', context)

def service(request):
    setting = Setting.objects.get()
    context = {'setting':setting, 'page':'service'}
    return render(request, 'service.html', context)
def appointment(request):
    setting = Setting.objects.get()
    context = {'setting':setting, 'page':'appointment'}
    return render(request, 'appointment.html', context)
def contact(request):
    if request.method=='POST':
        form=ContactFormu(request.POST)
        if form.is_valid():
            data=ContactFormMessage()
            data.name=form.cleaned_data['name']
            data.emai = form.cleaned_data['emai']
            data.subject=form.cleaned_data['subject']
            data.message = form.cleaned_data['message']
            data.save()
            messages.success(request,"mesajınız başarılı gönderilmiştir")
            return HttpResponseRedirect('/contact')
    setting =Setting.objects.get()
    form =ContactFormu()
    context={'setting':setting,'form':form}
    return render(request,'contact.html',context)
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request ,username=username, password=password)
        if user is not None:
            login(request,user)
            return HttpResponseRedirect('/')
        else:
            messages.warning(request,"giriş başaısız")
            return HttpResponseRedirect('/Login')
    return render(request,'Login.html')
def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username = username, password = password)
            login(request, user)
            return HttpResponseRedirect('/')

    form = SignUpForm()
    context = {'form': form}
    return render(request, 'signup.html', context)