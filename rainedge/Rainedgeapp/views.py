from django.shortcuts import render
from .models import Admission,Contact
from django.contrib.admin.views.decorators import staff_member_required
from students.models import Student
from teachers.models import Teacher
from courses.models import Course
from grades.models import Grade


def index(request):
    return render(request,'index.html')

def contact(request):
    return render(request,'contact.html')
def about(request):
    return render(request,'about.html')
def admissions(request):
    return render(request,'admissions.html')
def services(request):
    return render(request,'services.html')
def secondary(request):
    return render(request,'secondary.html')
def facilities(request):
    return render(request,'campus-facilities.html')
def events(request):
    return render(request,'events.html')
def news(request):
    return render(request,'news.html')
def privacy(request):
    return render(request,'privacy.html')
def students(request):
    return render(request,'students-life.html')
def contact(request):
    return render(request,'contact.html')
def alumni(request):
    return render(request,'alumni.html')
def four(request):
    return render(request,'404.html')
def academics(request):
    return render(request,'academics.html')
def primary(request):
    return render(request,'primary.html')
def maps(request):
    return render(request,'maps.html')

def admissions (request):
    if request.method == "POST" :
        full_name = request.POST.get("full__name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        program_interest = request.POST.get("program_interest")
        message = request.POST.get("message")

        Admission.objects.create(
            full_name=full_name,
            email=email,
            phone=phone,
            program_interest=program_interest,
            message=message,
        )
        return render(request, "admissions.html")
    
      # <-- FIX: Add return for GET requests
    return render(request, "admissions.html")


def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone_number = request.POST.get("phone_number")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        Contact.objects.create(
            name=name,
            email=email,
            phone_number=phone_number,
            subject=subject,
            message=message,
        )
        return render(request, "contact.html")
    
      #  Adds return for GET requests
    return render(request, "contact.html")

@staff_member_required
def admin_dashboard(request):
    total_students = Student.objects.count()
    total_teachers = Teacher.objects.count()
    total_courses = Course.objects.count()
    total_grades = Grade.objects.count()

    return render(request, 'portal/admin_dashboard.html',{
            'total_students': total_students,
            'total_teachers': total_teachers,
            'total_courses': total_courses,
            'total_grades':total_grades,
})




