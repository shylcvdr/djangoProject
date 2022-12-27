"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from home import views

urlpatterns = [
    path('', include('home.urls')),
    path('treatment/', include('treatment.urls')),
    path('home/', include('home.urls')),
    path('admin/', admin.site.urls),
    path(' ',include('home.urls')),
    path('about/', views.about,name='about'),
    path('contact/', views.contact,name='contact'),
    path('service/', views.service,name='service'),
    path('appointment/', views.appointment,name='appointment'),
    path('logout/',views.logout_view,name='logout_view'),
    path('Login/',views.login_view,name='login_view'),
    path('signup/', views.signup_view, name = 'signup_view'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
