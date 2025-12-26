from django.shortcuts import render, redirect
from .forms import attendanceForm
from .models import attendance 
from django.contrib.auth.decorators import login_required

@login_required
def mark_attendance (request) :
    if request.method == 'POST':
        form = attendanceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('teacher_attendance')
    else:
        form = attendanceForm()
    return render(request, 'attendance/mark_attendance.html', {'form':form})        

@login_required
def teacher_attendance(request):
    records = attendance.objects.filter(course_teacher= request.user.teacher)
    return render(request, 'attendance/teacher_attendance.html', {'records':records})

@login_required
def student_attendance(request):
    records = attendance.objects.filter(student=request.user.student)
    return render(request, 'attendance/student_attendance.html', {'records': records})