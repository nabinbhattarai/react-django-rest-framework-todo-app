from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TodoSerializer
from .models import Todo
# Create your views here.
@api_view(['GET'])
def apiOverview(request):
	api_urls = {
		'Create':'/create-todo/',
		'List':'/list-todo/',
		'Detail View':'/detail-todo/<str:pk>/',
		'Update':'/update-todo/<str:pk>/',
		'Delete':'/delete-todo/<str:pk>/',
		}


	return Response()

@api_view(['POST'])
def createTodo(request):
	serializer = TodoSerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

@api_view(['GET'])
def listTodo(request):
	todos = Todo.objects.all().order_by('-id')
	serializer = TodoSerializer(todos, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def detailTodo(request, pk):
	todos = Todo.objects.get(id=pk)
	serializer = TodoSerializer(todos, many=False)
	return Response(serializer.data)


@api_view(['POST'])
def updateTodo(request, pk):
	todos = Todo.objects.get(id=pk)
	serializer = TodoSerializer(instance=todos, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

@api_view(['DELETE'])
def deleteTodo(request, pk):
	todos = Todo.objects.get(id=pk)
	todos.delete()

	return Response('Item succsesfully delete!')