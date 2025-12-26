from django import forms
from .models import attendance

class attendanceForm(forms.ModelForm):
    class Meta:
        model = attendance
        fields = ['student', 'course', 'present']