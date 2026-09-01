from rest_framework.routers import DefaultRouter
from . import viewsets

router = DefaultRouter()
router.register('Category', viewsets.CategoryViewSet, basename='category')
router.register('Expense', viewsets.ExpenseViewSet, basename='expense')
urlpatterns = router.urls
