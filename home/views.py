from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    text = " Django kurulumu: python -m pip install Django<br> Proje oluşturma: django-admin startproject djangoproje<br> app ekleme: python manage.py startapp home"
    context = {'text': text}
    return render(request, 'index.html', context)