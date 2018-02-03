from django.shortcuts import render

# Create your views here.
from . import models
from . import serializers
from rest_framework import generics

class ListTodo(generics.ListCreateAPIView):
    queryset = models.Todo.objects.all()
    serializer_class = serializers.TodoSerializer

class DetailTodo(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Todo.objects.all()
    serializer_class = serializers.TodoSerializer
