from django.shortcuts import render
from todos.serializers import TaskSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from todos.models import Task
# Create your views here.


class TaskApiView(ListCreateAPIView): # Create and List with one class
    serializer_class = TaskSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        return Task.objects.filter(owner=self.request.user)
    

class TaskDetailApiView(RetrieveUpdateDestroyAPIView): # Retrieve, Update and Destroy with one class
    serializer_class = TaskSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = 'id'

    def get_queryset(self):
        return Task.objects.filter(owner=self.request.user)

