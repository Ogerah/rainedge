from django import forms
from django.contrib.auth.models import User
from students.models import Student


class StudentSignupForm( forms.ModelForm):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Student
        fields = ['student_id', 'gender', 'date_of_birth', 'phone','address', 'class_level', 'admission_date']