from django.shortcuts import render
from rest_framework.decorators import api_view , permission_classes
from rest_framework.response import Response
from .models import Task
from .serializers import TaskSerializer
from .serializers import RegisterSerializer
from drf_spectacular.utils import extend_schema
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
# Create your views here.

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_tasks(request):
    """
    Retrieve all tasks.
    """
    tasks = Task.objects.filter(owner=request.user)
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)
@extend_schema(request=TaskSerializer, responses=TaskSerializer)
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_task(request):
    """
    Create a new task.
    """
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(owner=request.user)
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@extend_schema(request=TaskSerializer, responses=TaskSerializer)
@api_view(['GET', 'PUT', 'DELETE','PATCH'])
@permission_classes([IsAuthenticated])
def task_detail(request, pk):
    try :
        task = Task.objects.get(pk=pk)
    except Task.DoesNotExist:
        return Response({'error': 'Task not found'}, status=404)
    if request.method == 'GET':
        serializer = TaskSerializer(task)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    elif request.method == 'PATCH' :
        serializer = TaskSerializer(task, data=request.data , partial=True)
        if serializer.is_valid() :
            serializer.save()
            return Response(serializer.data)
    elif request.method == 'DELETE':
        task.delete()
        return Response(status=204)

@extend_schema(request=RegisterSerializer, responses=RegisterSerializer)
class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({
                'username': user.username,
                'email': user.email
            }, status=201)
        return Response(serializer.errors, status=400)

    
class TaskProtectedView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({"message": "คุณเข้าถึงได้ เพราะคุณ login แล้ว"})