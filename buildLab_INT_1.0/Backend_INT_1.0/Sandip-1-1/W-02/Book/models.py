from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
    title=models.CharField(max_length=200)
    author=models.CharField()
    genre=models.CharField()
    published_year=models.IntegerField()
    user=models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )


    def __str__(self):
        return self.title

