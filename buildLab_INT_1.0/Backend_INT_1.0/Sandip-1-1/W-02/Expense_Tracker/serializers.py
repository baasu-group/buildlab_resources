from .models import Category, Expense
from rest_framework import serializers

class CategorySerializer(serializers.ModelSerializer):
    Category=serializers.CharField(source='category.name',read_only=True)
    
    class Meta:
        model=Category
        fields=[
            'id',
            'name',
            'user'
        ]

        read_only_fields=['id']

class ExpenseSerializer(serializers.ModelSerializer):
    Category_name=serializers.CharField(source='category.name',read_only=True)

    class Meta:
        model=Expense
        fields=[
            'id',
            'title',
            'amount',
            'category',
            'expense_date',
            'user'
        ]

        read_only_fields=['id']