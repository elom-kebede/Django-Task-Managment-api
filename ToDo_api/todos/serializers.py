from rest_framework.serializers import ModelSerializer
from todos. models import Task


class TaskSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = ('id','title', 'description', 'is_completed',)