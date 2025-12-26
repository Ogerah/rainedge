from django.urls import path
from . import views

urlpatterns= [
    path('teacher/', views.teacher_grades, name='teacher_grades'),
    path('teacher/add/', views.add_grade, name='add_grade'),
    path('student/', views.student_grades, name='students_grades'),
]