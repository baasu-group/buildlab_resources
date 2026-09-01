from rest_framework.routers import DefaultRouter
from . import viewsets

router = DefaultRouter()
router.register('categories', viewsets.CategoryViewSet, basename='category')
router.register('expenses', viewsets.ExpenseViewSet, basename='expense')
urlpatterns = router.urls