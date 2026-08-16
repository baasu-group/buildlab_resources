from django.contrib import admin
from django.urls import path
from W_01_Practice import api_views
from rest_framework_simplejwt.views import(
    TokenObtainPairView,
    TokenRefreshView
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/todos/',api_views.api_todo_list,name='api_todo_list'),
    path('api/todos/create/',api_views.api_todo_create,name='api_todo_create'),
    path('api/todos/<int:id>/update/',api_views.api_todo_update,name='api_todo_update'),
    path('api/todos/<int:id>/delete/',api_views.api_todo_delete,name='api_todo_delete'),
    path('api/token/',TokenObtainPairView.as_view(),name='token_obtain_pair'),
    path('api/token/refresh/',TokenRefreshView.as_view(),name='token_refresh'),
]
