from django.shortcuts import render, redirect
from .forms import TimetableForm
from .models import Timetable
from django.contrib.auth.decorators import login_required

@login_required
def add_timetable(request):
    if request.method == 'POST':
         form = TimetableForm(request.POST)
         if form.is_valid():
           form.save()
           return redirect('teacher_timetable')
    else:
        form = TimetableForm()
    return render(request, 'timetable/add_timetable.html',{'form':form})    

@login_required
def teacher_timetable(request):
    records = Timetable.objects.filter(course_teacher=request.user.teacher)
    return render(request, 'timetable/teacher_timetable.html', {'records': records})

@login_required
def student_timetable(request):
    records = Timetable.objects.filter(course_students=request.user.student)
    return render(request, 'timetable/student_timetable.html',{'records':records})
