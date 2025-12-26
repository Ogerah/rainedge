from django.urls import path
from . import views

urlpatterns = [
  path('create/', views.create_teacher, name='create_teacher'),
  path('dashboard/', views.dashboard, name= 'teacher_dashboard'),


]