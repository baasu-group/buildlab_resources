from rest_framework.routers import DefaultRouter
from . import viewsets

router = DefaultRouter()
router.register('books', viewsets.BookViewSet, basename='book')
urlpatterns = router.urls