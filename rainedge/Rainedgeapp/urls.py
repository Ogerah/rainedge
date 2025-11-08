"""
URL configuration for rainedge project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path

from Rainedgeapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
     path('index', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('admissions/', views.admissions, name='admissions'),
    path('services/', views.services, name='services'),
    path('', views.starter, name='starter'),
    path('campus-facilities/', views.facilities, name='facilities'),
    path('events/', views.events, name='events'),
    path('news/', views.news, name='news'),
    path('privacy/', views.privacy, name='privacy'),
    path('students-life/', views.students, name='students'),
    path('contact/', views.contact, name='contact'),
    path('alumni/', views.alumni, name='alumni'),
    path('404/', views.four, name='four'),
    path('academics/', views.academics, name='academics'),
]
