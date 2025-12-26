from django.urls import path
from . import views

urlpatterns = [
    path('teacher/', views.teacher_attendance, name='teacher_attendance'),
    path('teacher/mark/', views.mark_attendance, name='mark_attendance'),
    path('student/', views.student_attendance, name='student_attendance'),
]
