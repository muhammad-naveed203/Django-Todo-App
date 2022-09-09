from django.http import Http404
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import TodoList, TodoItem
from .serializers import TodoSerializer, TodoItemSerializer


class TodoListView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        user = request.user.id
        todo_list = TodoList.objects.filter(user=user)
        serializer = TodoSerializer(todo_list, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = dict(request.data)
        data["user"] = request.user.id
        serializer = TodoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ListDetail(APIView):
    permission_classes = (IsAuthenticated,)

    def get_object(self, pk, user):
        try:
            return TodoList.objects.get(pk=pk, user=user)
        except TodoList.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        user = request.user.id
        todo = self.get_object(pk, user)
        serializer = TodoSerializer(todo)
        return Response(serializer.data)


class TodoPublic(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        pub_todo = TodoList.objects.filter(privacy="public")
        serializer = TodoSerializer(pub_todo, many=True)
        return Response(serializer.data)


class MyPublic(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        user = request.user.id
        pub_todo = TodoList.objects.filter(user=user, privacy="public")
        serializer = TodoSerializer(pub_todo, many=True)
        return Response(serializer.data)


class ItemListView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        user = request.user.id
        todo_list = TodoItem.objects.filter(user=user)
        serializer = TodoItemSerializer(todo_list, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = dict(request.data)
        data["user"] = request.user.id
        serializer = TodoItemSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ItemDetail(APIView):
    permission_classes = (IsAuthenticated,)

    def get_object(self, pk, user):
        try:
            return TodoItem.objects.get(pk=pk, user=user)
        except TodoItem.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        user = request.user.id
        todo = self.get_object(pk, user)
        serializer = TodoItemSerializer(todo)
        return Response(serializer.data)


