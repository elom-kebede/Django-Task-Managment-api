from django.urls import path
from .views import TaskApiView, TaskDetailApiView

urlpatterns = [
    path('',TaskApiView.as_view(),name='task-list-create'),
    path('<int:id>/',TaskDetailApiView.as_view(),name='task-detail'),
    ]