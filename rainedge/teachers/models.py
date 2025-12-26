from django.db import models
from django.contrib.auth.models import User

class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    teacher_id = models.CharField(max_length=20, unique=True)
    phone = models.CharField(max_length=20, blank=True)
    address = models.TextField(blank=True)
    department = models.CharField(max_length=100)
    hire_date = models.DateField()
    profile_image = models.ImageField(upload_to= 'teachers/', default= 'teachers/default.png')
    
    def __str__(self):
        return f"{self.user.first_name}{self.user.last_name}"
    
