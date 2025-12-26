from django.shortcuts import render, redirect
from .models import Course
from .forms import CourseForm
from django.contrib.auth.decorators import login_required
from students.models import Student

@login_required
def teacher_course_list(request):
    courses = Course.objects.filter(teacher=request.user.teacher)
    return render(request, 'courses/teacher_course_list.html',{'courses':courses})

@login_required
def add_course(request):
    if request.method =='POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            course = form.save(commit=False)
            course.teacher = request.user.teacher
            course.save()
            return redirect ('teacher_course_list')
        
    else:
        form = CourseForm()
    return render(request, 'courses/add_course.html', {'form':form})   

@login_required
def student_course_list(request):
    student = request.user.student
    courses = Course.objects.all()
    enrolled_courses = student.course_set.all()
    return render( request, 'courses/student_course_list.html',{
     'courses': courses,
     'enrolled_courses':enrolled_courses
    } )

@login_required
def enroll_course(request, course_id):
    student = request.user.student
    course = Course.objects.get (id= course_id)
    course.students.add(student)
    return redirect('student_course_list')
