from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Todo
from .serializers import TodoSerializer

class TodoViewSet(viewsets.ModelViewSet):
    serializer_class=TodoSerializer
    permission_classes=[permissions.IsAuthenticated]

    def get_queryset(self):
        return Todo.objects.filter(
            user=self.request.user
        ).order_by('-created_at')

    def perform_create(self,serializer):    #creating the posts i.e updating forms etc
        serializer.save(user=self.request.user)

    def get_permissions(self):
        if self.action == 'list':
            return [permissions.IsAuthenticated()]
        return [permissions.IsAuthenticated()]

    @action(detail=False,methods=['get'])
    def completed(self,request):        #custom api call except simple ones
        todos=self.get_queryset().filter(completed=True)
        serializer= self.get_serializer(todos,many=True)
        return Response(serializer.data)

    @action(detail=False ,methods=['get'])
    def pending(self,request):
        todos=self.get_queryset().filter(completed=False)
        serializer= self.get_serializer(todos,many=True)
        return Response(serializer.data)

