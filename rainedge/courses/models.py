from django.db import models
from teachers.models import Teacher
from students.models import Student

from django.db import models
from students.models import Student  # adjust import if needed

class Course(models.Model):
    name = models.CharField(max_length=100)

    students = models.ManyToManyField(
        Student,
        through='Enrollment',
        related_name='courses'
    )

    def __str__(self):
        return self.name


class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    enrolled_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student} → {self.course}"

