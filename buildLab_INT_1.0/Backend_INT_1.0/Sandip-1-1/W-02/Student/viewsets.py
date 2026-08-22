from rest_framework import permissions, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Avg, Count
from .serializers import StudentSerializer, GradeSerializer
from .models import Student, Grade

class StudentViewSet(viewsets.ModelViewSet):
    serializer_class = StudentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Student.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=True, methods=['get'])
    def report(self, request, pk=None):
        student = self.get_object()
        grades = student.grades.all()
        stats = grades.aggregate(
            average_score=Avg('score'),
            total_subjects=Count('id')
        )
        grade_serializer = GradeSerializer(grades, many=True)
        return Response({
            'student': student.name,
            'average_score': stats['average_score'],
            'total_subjects': stats['total_subjects'],
            'grades': grade_serializer.data
        })


class GradeViewSet(viewsets.ModelViewSet):
    serializer_class = GradeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Grade.objects.filter(student__user=self.request.user)

    def perform_create(self, serializer):
        serializer.save()

    @action(detail=False, methods=['get'])
    def failing(self, request):
        grades = self.get_queryset().filter(score__lt=50)
        serializer = self.get_serializer(grades, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def by_subject(self, request):
        subject = request.query_params.get('subject', None)
        if subject:
            grades = self.get_queryset().filter(subject=subject)
        else:
            grades = self.get_queryset()
        serializer = self.get_serializer(grades, many=True)
        return Response(serializer.data)