from django.urls import path
from . import views

urlpatterns = [
    path('teacher/', views.teacher_timetable, name='teacher_timetable'),
    path('teacher/add/', views.add_timetable, name='add_timetable'),\
    path('student/', views.student_timetable, name='student_timetable'),
]
