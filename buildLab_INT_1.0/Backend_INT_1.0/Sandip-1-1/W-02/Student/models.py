from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator




class Student(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField()
    user=models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )


    def __str__(self):
        return self.name

class Grade(models.Model):
    student=models.ForeignKey(
        'Student',
        on_delete=models.CASCADE,
        related_name='grades'
    )
    subject=models.CharField(max_length=150)
    score=models.FloatField(
        validators=[MinValueValidator(0),MaxValueValidator(100)]
    )
    grade_date=models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.name} - {self.subject}"


