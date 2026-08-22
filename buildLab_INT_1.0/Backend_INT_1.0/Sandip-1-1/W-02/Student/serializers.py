from .models import Student,Grade
from rest_framework import serializers

class StudentSerializer(serializers.ModelSerializer):
    username=serializers.CharField(source='user.username',read_only=True)

    class Meta:
        model=Student
        fields=[
            'id',
            'name',
            'email',
            'username'
        ]

        read_only_fields=['id']


class GradeSerializer(serializers.ModelSerializer):
    student_name =serializers.CharField(source='student.name',read_only=True)

    class Meta:
        model=Grade
        fields=[
            'id',
            'student',
            'subject',
            'score',
            'grade_date',
            'student_name'
        ]

        read_only_fields=['grade_date','id']