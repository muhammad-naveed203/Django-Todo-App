from django.urls import path

from .views import TodoListView, TodoPublic, MyPublic, ItemDetail, ListDetail, ListItems

urlpatterns = [

    path('api/todo_list/', TodoListView.as_view()),
    path('api/todo_list/<int:pk>/', ListDetail.as_view()),
    path('api/todo_list/pub_todos/', TodoPublic.as_view()),
    path('api/todo_list/my_public/', MyPublic.as_view()),
    path('api/list/<int:pk>/items/', ListItems.as_view()),
    path('api/item/<int:pk>/', ItemDetail.as_view()),


]
