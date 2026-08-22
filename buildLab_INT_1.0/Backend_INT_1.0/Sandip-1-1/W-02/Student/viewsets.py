from rest_framework import permissions,viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import StudentSerializer,GradeSerializer
from .models import Student,Grade

class StudentViewSet(viewsets.ModelViewSet):
    serializer_class=StudentSerializer
    permission_classes=[permissions.IsAuthenticated]

    def get_queryset(self):
        return Student.objects.filter(
            user=self.request.user 
        )

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_permissions(self):
        if self.action == 'list':
            return [permissions.IsAuthenticated()]
        return [permissions.IsAuthenticated()]

    @action(detail=True,methods=['get'])
    def report(self,request):


class GradeViewSet(viewsets.ModelViewSet):
    serializer_class=GradeSerializer
    permission_classes=[permissions.IsAuthenticated]

    def get_queryset(self):
        