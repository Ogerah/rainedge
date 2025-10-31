from django.shortcuts import render

def index(request):
    return render(request,'index.html')
def contact(request):
    return render(request,'contact.html')
def about(request):
    return render(request,'about.html')
def admissions(request):
    return render(request,'admissions.html')
def services(request):
    return render(request,'terms-of-service.html')
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


