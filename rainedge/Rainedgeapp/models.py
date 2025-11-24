from django.db import models

class Admission(models.Model):
    full_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=50, blank=True)
    program_interest = models.CharField(max_length=10)
    message = models.TextField(blank=True)
    
    def __str__(self):
        return self.full_name
    