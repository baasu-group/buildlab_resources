from rest_framework import viewsets,permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Book
from .serializers import BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    serializer_class=BookSerializer
    permission_classes=[permissions.IsAuthenticated]

    def get_queryset(self):
        return Book.objects.filter(
            user=self.request.user
        ).order_by('-published_year')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_permissions(self):
        if self.action == 'list':
            return [permissions.IsAuthenticated()]
        return [permissions.IsAuthenticated()]

    @action(detail=False,methods=['get'])
    def by_genre(self,request):
        books=self.get_queryset().filter(genre='fiction')
        serializer=self.get_serializer(books,many=True)
        return Response(serializer.data)
    