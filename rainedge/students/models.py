from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    student_id = models.CharField(max_length=20, unique=True)
    gender = models.CharField(max_length= 10, choices= [('Male','Male'), ('Female','Female')])
    date_of_birth = models.DateField(null=True, blank=True)


    phone= models.CharField(max_length=20, blank=True)
    address = models.TextField(blank=True)

    class_level = models.CharField(max_length= 50)
    admission_date = models.DateField()

    profile_image = models.ImageField(upload_to='students/', default='students/default.png')

    def __str__(self):
        return f" {self.user.first_name} {self.user.last_name} - {self.student_id}"
