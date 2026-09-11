from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=150)
    age = models.IntegerField()
    email = models.EmailField(max_length=254)
    course = models.CharField( max_length=50)

class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=5, decimal_places=2)


# Create your models here.
