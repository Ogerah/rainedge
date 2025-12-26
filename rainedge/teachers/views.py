from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import user_passes_test
from .forms import TeacherForm
from django.contrib.auth.decorators import login_required

def is_admin(user):
    return user.is_superuser

@user_passes_test(is_admin)
def create_teacher(request):
    if request.method =='POST':
        form = TeacherForm(request.POST, request.FILES)
        if form.is_valid():
            user = User.objects.create_user(
              username=form.cleaned_data['email'],
              email=form.cleaned_data['email'],
              first_name=form.cleaned_data['first_name'],
              last_name=form.cleaned_data['last_name'],
              password=form.cleaned_data['password']
           )
            teacher = form.save(commit=False)
            teacher.user = user
            teacher.save()

            return redirect('teacher_list')
        
    else:
        form = TeacherForm()

    return render(request, 'teachers/create_teacher.html',{'form':form})     

@login_required
def dashboard(request):
    return render(request, 'teachers/dashboard.html')


