from .models import Category, Expense
from rest_framework import serializers

class CategorySerializer(serializers.ModelSerializer):    
    class Meta:
        model=Category
        fields=[
            'id',
            'name',
        ]

        read_only_fields=['id']

class ExpenseSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name', read_only=True)

    class Meta:
        model = Expense
        fields = ['id', 'title', 'amount', 'category', 'category_name', 'expense_date']
        read_only_fields = ['id', 'expense_date']
        