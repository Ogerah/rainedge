from django import forms
from django.contrib.auth.models import User
from .models import Teacher

class TeacherForm(forms.ModelForm):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Teacher
        fields = ['teacher_id', 'phone', 'address', 'department', 'hire_date']

        