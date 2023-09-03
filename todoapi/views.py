
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from todoapi.models import Todo
from todoapi.serializers import TodoSerializer


@api_view(['GET'])
def home(request):
    myapi_urls = {
        'List': '/todo-list/',
        'Detail View': '/todo-detail/<int:pk>/',
        'Create': '/todo-create/',
        'Update': '/todo-update/<int:pk>/',
        'Delete': '/todo-delete/<int:pk>/',
    }
    return Response(myapi_urls)


@api_view(['GET'])
def list_view(request):
    todos = Todo.objects.all()
    serializer = TodoSerializer(todos, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def detail_view(request, pk):
    todo = Todo.objects.get(id=pk)
    serializer = TodoSerializer(todo, many=False)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def create_view(request):
    serializer = TodoSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['POST'])
def update_view(request, pk):
    todo = Todo.objects.get(id=pk)
    serializer = TodoSerializer(instance=todo, data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data, status=status.HTTP_202_ACCEPTED)


@api_view(['DELETE'])
def delete_view(request, pk):
    todo = Todo.objects.get(id=pk)
    todo.delete()
    return Response("Todo deleted successfully", status=status.HTTP_204_NO_CONTENT)
