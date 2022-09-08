from django.http import Http404
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import TodoList, TodoItem
from .serializers import TodoSerializer, TodoitemSerializer


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


class TodoPublic(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        pub_todo = TodoList.objects.filter(privacy="public")
        serializer = TodoSerializer(pub_todo, many=True)
        return Response(serializer.data)


class ItemListView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        user = request.user.id
        todo_list = TodoItem.objects.filter(id=user)
        serializer = TodoitemSerializer(todo_list, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = dict(request.data)
        data["user"] = request.user.id
        serializer = TodoitemSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ItemDetail(APIView):
    permission_classes = (IsAuthenticated,)

    def get_object(self, pk):
        try:
            return TodoItem.objects.get(pk=pk)
        except TodoItem.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        todo = self.get_object(pk)
        serializer = TodoitemSerializer(todo)
        return Response(serializer.data)


