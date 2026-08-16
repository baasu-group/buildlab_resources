from rest_framework import status
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.response import Response 
from .models import Todo
from .serializers import TodoSerializer

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def api_todo_list(request,):
    try:
        todos = Todo.objects.filter(user=request.user).order_by('-created_at')
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data)
    except Todo.DoesNotExist:
        return Response({'error':'No TODOS'},status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def api_todo_create(request):
    serializer=TodoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def api_todo_update(request,id):
    try:
        post=Todo.objects.get(id=id)
    except Todo.DoesNotExist:
        return Response({'error':'Post Not Found'},status=status.HTTP_404_NOT_FOUND)
    if post.user!=request.user:
        return Response({'error':'Not Allowed'},status=status.HTTP_403_FORBIDDEN)
    serializer=TodoSerializer(post,data=request.data,partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def api_todo_delete(request,id):
    try:
        post=Todo.objects.get(id=id)
    except Todo.DoesNotExist:
        return Response({'error':'Post Not Found'},status=status.HTTP_404_NOT_FOUND)
    if post.user!=request.user:
        return Response({'error':'Not Allowed'},status=status.HTTP_403_FORBIDDEN)
    post.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)