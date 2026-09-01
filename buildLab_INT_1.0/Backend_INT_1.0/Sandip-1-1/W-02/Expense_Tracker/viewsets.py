from rest_framework import permissions, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Sum, Count
from .serializers import CategorySerializer, ExpenseSerializer
from .models import Category, Expense
from datetime import datetime

class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class= CategorySerializer
    permission_classes=[permissions.IsAuthenticated]

    def get_queryset(self):
        return Category.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ExpenseViewSet(viewsets.ModelViewSet):
    serializer_class= ExpenseSerializer
    permission_classes=[permissions.IsAuthenticated]

    def get_queryset(self):
        return Expense.objects.filter(user=self.request.user)

    def perform_create(self,serializer):
        serializer.save(user=self.request.user)

    @action(detail=False, methods=['get'])
    def total(self,request):
        total_expense=self.get_queryset().aggregate(total_amount=Sum('amount'))
        return Response({
            "Total": total_expense['total_amount'] or 0
        })

    @action(detail=False, methods=['get'])
    def by_category(self,request):
        category=request.query_params.get('category',None)
        if category:
            expenses=self.get_queryset().filter(category__name=category)
        else:
            expenses=self.get_queryset()
        serializer=self.get_serializer(expenses,many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def this_month(self,request):
        month=request.query_params.get('month',None)
        if month:
            expenses=self.get_queryset().filter(expense_date__month=month)
        else:
            current_month=datetime.now().month
            expenses=self.get_queryset().filter(expense_date__month=current_month)
        serializer=self.get_serializer(expenses,many=True)
        return Response(serializer.data)

    