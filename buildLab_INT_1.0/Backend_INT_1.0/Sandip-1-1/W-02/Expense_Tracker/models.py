from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name=models.CharField(max_length=200)
    user=models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name
    

class Expense(models.Model):
    title=models.CharField(max_length=200)
    amount=models.DecimalField(max_digits=10,decimal_places=2)
    category=models.ForeignKey(
        'Category',
        on_delete=models.CASCADE,
        related_name='expenses'
    )
    expense_date=models.DateField(auto_now_add=True)
    user=models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title