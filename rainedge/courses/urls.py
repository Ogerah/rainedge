from django.urls import path
from .import views

urlpatterns = [
    #for Teachers
    path('teacher/', views.teacher_course_list, name='teacher_course_list'),
    path('teacher/add/', views.add_course, name='add_course'),

    #for Student
    path('student/', views.student_course_list, name='student_course_list'),
    path ('student/enroll/<int:course_id/', views.enroll_course, name='enroll_course'),
]
