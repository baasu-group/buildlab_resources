from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (TokenRefreshView,TokenObtainPairView)
from django.contrib import admin
from django.urls import path,include
from Book import viewsets
import Book
import Student

router=DefaultRouter()
router.register('books',viewsets.BookViewSet,basename='book')

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/",include(Book.urls)),
    path("api/",include(Student.urls)),
    path('api/token/',TokenObtainPairView.as_view(),name='token_obtain_pair'),
    path('api/token/refresh/',TokenRefreshView.as_view(),name='token_refresh'),
]
