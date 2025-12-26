from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .forms import StudentSignupForm
from students.models import Student
from django.contrib.auth import authenticate,login, logout
from teachers.models import Teacher

def signup_view(request):
    if request.method == 'POST':
        form = StudentSignupForm(request.POST, request.FILES)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data['email'],
                email=form.cleaned_data['email'],
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                password=form.cleaned_data['password']
            )

            student = form.save(commit=False)
            student.user = user
            student.save()

            login(request,user)
            return redirect('student_dashboard')
        else:
            form = StudentSignupForm()

            return render(request, 'accounts/templates/signup.html', {'form': form}) 
def login_view(request):
    error = None

    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']   

        user = authenticate(username=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('student_dashboard')
        else:
            error = "Invalid email or password"

    return render(request, 'accounts/templates/login.html' , {'error': error})

def logout_view(request):
    logout(request)
    return redirect('login')

def teacher_login(request):
    error = None

    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(username=email, password=password)

        if user is not None:
            if hasattr(user,'teacher'):
                login(request,user)
                return redirect('teacher_dashboard')
            else:
                error = "You are not registered as a teacher."
        else:
            error = "Invalid email or password."

    return render(request, 'accounts/templates/teacher_login.html', {'error':error})                
 


