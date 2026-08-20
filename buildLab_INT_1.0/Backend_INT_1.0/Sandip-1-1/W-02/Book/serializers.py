from models import Book
from rest_framework import serializers

class BookSerializer(serializers.ModelSerializer):
    username=serializers.CharField(source='user.username',read_only=True)

    class Meta:
        model=Book
        fields=[
            'id',
            'title',
            'author',
            'genre',
            'published_year',
            'username'
        ]
        read_only_fields=['id']