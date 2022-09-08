from rest_framework import serializers
from .models import TodoList, TodoItem


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoList
        fields = '__all__'


class TodoitemSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoItem
        fields = '__all__'
