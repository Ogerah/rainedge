from django.db import models
from courses.models import Course

class Timetable(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    day_of_week = models.CharField(max_length=10, choices=[
        ('Monday', 'Monday'),('Tuesday','Tuesday'),('Wednesday','Wednesday'),
        ('Thursday','Thuersday'),('Friday','Friday')
    ])
    start_time = models.TimeField()
    end_time = models.TimeField()
    room = models.CharField(max_length=50, blank=True)

    
    def __str__(self):
        return f"{self.course.name} on {self.day_of_week} ({self.start_time}-{self.end_time}"
