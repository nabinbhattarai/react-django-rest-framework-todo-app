from django.urls import path
from . import views

urlpatterns = [
	path('', views.apiOverview, name="api-overview"),
	path('list-todo/', views.listTodo, name="listTodo"),
	path('detail-todo/<str:pk>/', views.detailTodo, name="detailTodo"),
	path('create-todo/', views.createTodo, name="createTodo"),
	path('update-todo/<str:pk>/', views.updateTodo, name="updateTodo"),
	path('delete-todo/<str:pk>/', views.deleteTodo, name="deleteTodo"),
]
