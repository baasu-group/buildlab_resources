from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (TokenRefreshView,TokenObtainPairView)
from django.contrib import admin
from django.urls import path,include
from Book import viewsets

router=DefaultRouter()
router.register('books',viewsets.BookViewSet,basename='book')

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/",include(router.urls)),
    path('api/token/',TokenObtainPairView.as_view(),name='token_obtain_pair'),
    path('api/token/refresh',TokenRefreshView.as_view(),name='token_refresh'),
]
