from django.shortcuts import render
from .models import Admission

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
def starter(request):
    return render(request,'starter-page.html')
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






