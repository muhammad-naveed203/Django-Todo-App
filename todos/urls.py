from django.urls import path

from .views import TodoListView, TodoPublic, MyPublic, ItemListView, ItemDetail, ListDetail, ListItems

urlpatterns = [

    path('api/todo_list/', TodoListView.as_view()),
    path('api/todo_list/<int:pk>/', ListDetail.as_view()),
    path('api/todo_list/pub_todos/', TodoPublic.as_view()),
    path('api/todo_list/my_public/', MyPublic.as_view()),
    path('api/item/', ItemListView.as_view()),
    path('api/item/<int:pk>/', ItemDetail.as_view()),
    path('api/list_items/<int:pk>/', ListItems.as_view()),

]
