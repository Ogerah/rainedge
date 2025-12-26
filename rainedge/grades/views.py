from django.shortcuts import render, redirect
from .forms import GradeForm
from .models import Grade
from django.contrib.auth.decorators import login_required

@login_required
def add_grade(request):
    if request.method == 'POST':
        form = GradeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('teacher_grades')
    else:
        form = GradeForm()
    return render(request, 'grades/add_grade.html', {'form':form})

@login_required
def teacher_grades(request):
    grades= Grade.objects.filter(course_teacher=request.user.teacher)
    return render(request, 'grades/teacher_grades.html', {'grades':grades})

@login_required
def student_grades(request):
    grades = Grade.objects.filter(student=request.user.student)
    return render(request, 'grades/student_grades.html', {'grades': grades})        

