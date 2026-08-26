from rest_framework.routers import DefaultRouter
from . import viewsets

router = DefaultRouter()
router.register('students', viewsets.StudentViewSet, basename='student')
router.register('grades',viewsets.GradeViewSet,basename='grade')
urlpatterns = router.urls
